# �ؼ�����
```
bx lr		1E FF 2F E1
mov r0,#0	00 00 A0 E3
mov r0,#1	01 00 A0 E3
nop			00 00 A0 E1

dllBaseAddr ��ͨ��/proc/uid/maps�ļ���ȡ
if (sscanf(line, "%lx-%lx %c%c%c%c %x %x:%x %u %[^\n]", &start, &end, &read,
                &write, &exec, &cow, &offset, &dev_major, &dev_minor, &inode, filename) >= 6) 
		{
			char* str = NULL;
			str = strstr(filename, "libil2cpp.so");
			//fprintf(stderr, "find %x ~ %x; %s\n", start, end, filename);
			if (str)
			{
				 fprintf(stderr, "---find %x ~ %x; %s\n", start, end, filename);
				 dllBaseAddr = start;
				 //dllBaseAddr = (void *)(start + 0x70A5F0);
				 return true;
			}
           
        }
		

�޸Ĺؼ�������Ӧ�Ļ����룬д����ֽڵĻ�����

char ori_buf[]= {0x18, 0xB0, 0x8D, 0xE2, 0x08, 0xD0, 0x4D, 0xE2};
char buf[] = { 0x00, 0x00, 0xA0, 0xE3, 0x1E, 0xFF, 0x2F, 0xE1 };//����ָ�mov r0,#0 �� bx lr
void *data;
data = buf;

ptrace(PTRACE_POKEDATA, target_pid, (void *)(dllBaseAddr + 0x70A5F0 + 4), *(long *)(data + 0));//�ڵ�ַ0xBA4195F4д�������0x00 0x00 0xA0 0xE3
ptrace(PTRACE_POKEDATA, target_pid, (void *)(dllBaseAddr + 0x70A5F0 + 4+ 4), *(long *)(data + 4));//�ڵ�ַ0xBA4195F8д�������0x1E 0xFF 0x2F 0xE1

```
# �ؼ�������ô��λ
���ֿ���ͨ��GG��������λ�ؼ������ڴ��е�ʵ�ʵ�ַ�����libil2cpp.so����ʼ��ַ�����ƫ��       
���IDA��dnSpy����λ�������ߺ������ﵽ�޸ĵ�Ŀ�ģ�����ֻ�����this��ƫ�ƣ�       

```
��dnSpy����������
		// Token: 0x040029A9 RID: 10665
		[FieldOffset(Offset = "0x4C")]
		public int coin

��GG������ҵ��ڴ��ַ
��������
B3272FD4
B3272FD4 - b3266000 = CFD4
info: ### 120, size: 626688, name: , b3266000-b32ff000, type: 0

C1EEC944
C1EEC944 - c1ede000 = E944 		
info: ### 211, size: 626688, name: , c1ede000-c1f77000, type: 0

C30D397C
C30D397C - c30c4000 = F97C
info: ### 234, size: 626688, name: , c30c4000-c315d000, type: 0

�����ĵ�ַ������û���취���¶�λ
��size: 626688����ڴ�����棬����libil2cpp.so���ڴ�����棬����ÿ������ڴ������ƫ��Ҳ��һ��
```

# STR LDRָ��

```
STR{����}  Դ�Ĵ�����<�洢����ַ>
STRָ����ء��Դ�Ĵ����н�һ��32λ�������ݴ��͵��洢���С�

STR R0��[R1]����8             ����R0�е�������д����R1Ϊ��ַ�Ĵ洢���У������µ�ַR1��8д��R1��
STR R0��[R1����8]             ����R0�е�������д����R1��8Ϊ��ַ�Ĵ洢���С���
STR     r1, [r0]              ����r1�Ĵ�����ֵ�����͵���ֵַΪr0�ģ��洢�����ڴ���


LDR �Ӵ洢���м������ݵ��Ĵ���
LDR R3,=0X40000000;LDRαָ��ѵ�ַ���ص��Ĵ�������ȥ
LDR R4,[R3,#0x04];���׵�ַ����ƫ�����õ����ݵĵ�ַ��Ѱַ R3------->0x40000000+4=0x40000004----->4
ldr r0, =0x12345678
�������Ͱ�0x12345678�����ַд��r0���ˡ����ԣ�ldrαָ���mov�ǱȽ����Ƶġ�ֻ����movָ���������������ĳ���Ϊ8λ��Ҳ���ǲ��ܳ���512����ldrαָ��û��������ơ����ʹ��ldrαָ��ʱ���������������û�г�
```

# arm��ຯ�����ò������ݹ���	

```
arm��ຯ�����ò������ݹ���	
	 1. �ӳ���ͨ���Ĵ���R0~R3�����ݲ���. ��ʱ�Ĵ������Լ���: A0~A3 , �����õ��ӳ����ڷ���ǰ����ָ��Ĵ���R0~R3������.
     2. ���ӳ�����,ʹ��R4~R11������ֲ�����,��ʱ�Ĵ���R4~R11���Լ���: V1~V8 .������ӳ�����ʹ�õ�V1~V8��ĳЩ�Ĵ���,�ӳ������ʱ���뱣����Щ�Ĵ�����ֵ,�ڷ���ǰ����ָ���Щ�Ĵ�����ֵ,�����ӳ�����û���õ��ļĴ����򲻱�ִ����Щ����.��THUMB�����У�ͨ��ֻ��ʹ�üĴ���R4~R7������ֲ�����.
     3.�Ĵ���R12�����ӳ����scratch�Ĵ���,����ip; ���ӳ�������Ӵ�����о�����������ʹ�ù���.
     4. �Ĵ���R13��������ջָ��,����SP,���ӳ����мĴ���R13��������������;. �Ĵ���SP�ڽ����ӳ���ʱ��ֵ���˳��ӳ���ʱ��ֵ�������.
     5. �Ĵ���R14�������ӼĴ���,����lr ; �����ڱ����ӳ���ķ��ص�ַ,������ӳ����б����˷��ص�ַ,��R14��������������;.
     6. �Ĵ���R15�ǳ��������,����PC ; ����������������;.
     7. ATPCS�еĸ��Ĵ�����ARM�������ͻ�����ж���Ԥ�����.	
```

# IDA��̬����so����
https://www.bilibili.com/video/BV1ub411E7wS?from=search&seid=15387634077601357608      
```
�����ϵ����Ϸֱ��������

����������ķ���
	./data/local/tmp/android_server
	adb forward tcp:23946 tcp:23946	
	adb shell am start -D -n com.knight.union.aligames/com.chillyroom.plugin.wrapper4399.ActivityWrapper4399
	IDA���ӽ���
	C:\Java\jdk1.8.0_31\bin\jdb -connect com.sun.jdi.SocketAttach:hostname=localhost,port=8700
	
DDMS�޷���������
��ʱ������� ��� <application android:debuggable="true" ���´��
�޸�ro.debuggableΪ1 ������mprop�޸�ʧ��	

jdb -connect com.sun.jdi.SocketAttach:hostname=localhost,port=8700����ʾ
��������:
�޷����ӵ�Ŀ�� VM
```

# ʹ�����ֻ�IDA��̬����so

```
./data/local/tmp/android_server
adb forward tcp:23946 tcp:23946	
ֱ���ֻ���������Ϸ���浽����1
IDA���ӽ���

����ʱ���Խ���ϵ�

���ʹ��C:\Java\jdk1.8.0_31\bin\jdb -connect com.sun.jdi.SocketAttach:hostname=localhost,port=8700����
���ǻ���ʾ
��������:
�޷����ӵ�Ŀ�� VM
```