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
���IDA��dnSpy����λ�������ߺ������ﵽ�޸ĵ�Ŀ��       

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