#
```
��Ϸ���ֵ��ǻ�malloc һ���ڴ棬malloc���Σ�������Ѫ�Ϳ�

```

```
64����Ϸ���� ��
hook malloc������0x1408��С���ڴ��
Ѫ��ƫ�� =   0x130C;
�񱩵�ƫ�� = 0xD44;

��Ϸ����
---begin
0x1408
0x70b0b00800			(blood crazy)00000000 00000000
---end


---begin
0x1408
0x70b0b64800			(blood crazy)00000000 ff3300ff(-13434625)
---end


�������� �ڶ��μ���
---begin
0x1408
0x710a84a000			(blood crazy)0000002e 00000104
---end


---begin
0x1408
0x710a84a000			(blood crazy)00000000 00000104
---end


�������� ��������
---begin
0x1408
0x70bb56f000			(blood crazy)00000000 00000000
---end


---begin
0x1408
0x70bb56f000			(blood crazy)00000000 00000000
---end

��һ�η��������0x1408 ��ַ��һ��
�ڶ��η��������0x1408 ��ַһ��
�����η��������0x1408 ��ַһ��

ֱ��ÿ�θ��µ�ַ
```

```
32λ��Ϸ����
hook malloc������0x1008��С���ڴ��
Ѫ��ƫ�� =   0xF44;
�񱩵�ƫ�� = 0xAA4;


2020-09-16 19:20:55.156 26938-26938/? E/inlinehook: alternatvie DadNMe _bloodAddr _crazyAddr: ccb71f44 ccb71aa4 14198 1868784742
2020-09-16 19:20:55.572 26938-26989/? E/inlinehook: alternatvie DadNMe _bloodAddr _crazyAddr: b3bc6b44 b3bc66a4 0 0
2020-09-16 19:20:55.572 26938-26989/? E/inlinehook: alternatvie DadNMe _bloodAddr _crazyAddr: b1e0bf44 b1e0baa4 0 0
2020-09-16 19:20:55.574 26938-26989/? E/inlinehook: alternatvie DadNMe _bloodAddr _crazyAddr: b1e0e744 b1e0e2a4 0 0
2020-09-16 19:20:55.582 26938-26989/? E/inlinehook: alternatvie DadNMe _bloodAddr _crazyAddr: b1e0bf44 b1e0baa4 -1307031592 -1307032616
2020-09-16 19:20:55.594 26938-26989/? E/inlinehook: alternatvie DadNMe _bloodAddr _crazyAddr: b1e0e744 b1e0e2a4 -1310341600 0
2020-09-16 19:21:06.218 26938-26989/? E/inlinehook: alternatvie DadNMe _bloodAddr _crazyAddr: af0a4f44 af0a4aa4 1065353216 1			(important!!!!)		3F800000 00000001
2020-09-16 19:21:13.305 26938-26989/? E/inlinehook: +++update DadNMe _bloodAddr _crazyAddr: af0a4f44 af0a4aa4 1065353216 1146129076							3F800000 44508AB4
2020-09-16 19:21:25.418 26938-27041/? E/inlinehook: alternatvie DadNMe _bloodAddr _crazyAddr: b3451b44 b34516a4 0 0						(�˾���ܲ����м�)	00000000 00000000

2020-09-16 20:01:56.404 26938-26989/? E/inlinehook: alternatvie DadNMe _bloodAddr _crazyAddr: b4156744 b41562a4 0 0						(important!!!!)
2020-09-16 20:02:03.395 26938-26989/? E/inlinehook: +++update DadNMe _bloodAddr _crazyAddr: b4156744 b41562a4 0 0

2020-09-16 20:03:38.065 26938-26989/? E/inlinehook: +++update DadNMe _bloodAddr _crazyAddr: b4156744 b41562a4 0 0						(important!!!!)
2020-09-16 20:03:45.125 26938-26989/? E/inlinehook: +++update DadNMe _bloodAddr _crazyAddr: b4156744 b41562a4 0 0

2020-09-16 20:05:03.624 26938-26989/? E/inlinehook: +++update DadNMe _bloodAddr _crazyAddr: b4156744 b41562a4 0 0						(important!!!!)
2020-09-16 20:05:10.672 26938-26989/? E/inlinehook: +++update DadNMe _bloodAddr _crazyAddr: b4156744 b41562a4 0 0

2020-09-16 20:13:05.454 26938-26989/? E/inlinehook: alternatvie DadNMe _bloodAddr _crazyAddr: b4153f44 b4153aa4 0 0						(important!!!!)
2020-09-16 20:13:12.568 26938-26989/? E/inlinehook: +++update DadNMe _bloodAddr _crazyAddr: b4153f44 b4153aa4 0 0

_bloodAddr _crazyAddr:��ֵ���� 1065353216 1146129076�����µ�ַ �����  �˾�����м��ˣ�
�������ε�ַ��ͬ�����µ�ַ

ע���С�ˣ�������С�ˣ�С�ˣ���λ���ݴ���ڵ�λ��ַ
��frida�д�ӡ����������
---begin
0x1008
0xa5d32000
---blood value
           0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  0123456789ABCDEF
00000000  00 00 80 3f(��ӡ�ڴ��е�����: ��λ����->��λ����)...?					0x3f800000	д����ʱ�����ݵı�ʾ��0x��λ����...��λ����
---crazy value
           0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  0123456789ABCDEF
00000000  b4 8a 50 44                                      ..PD					0x448a5044
---end
```

```
32����Ϸ��Ӧ�ĵ�ַ�ж�
		if (0x1008 == size)
		{
			if (ret != _alternativeBaseAddr)
			{
				_alternativeBaseAddr = ret;
				LOGE("alternatvie DadNMe _bloodAddr _crazyAddr: %x %x %d %d\n", ret + nDeltaBlood32, ret + nDeltaCrazy32, 
				*(static_cast<unsigned int*>(ret + nDeltaBlood32)), *(static_cast<unsigned int*>(ret + nDeltaCrazy32)));
				unsigned int* addrTmp1 = static_cast<unsigned int*>(ret + nDeltaBlood32);
				unsigned int* addrTmp2 = static_cast<unsigned int*>(ret + nDeltaCrazy32);
				//LOGE("value: %d %d\n", (int)(*addrTmp1), (int)(*addrTmp2));
				if ((1065353216 == (*addrTmp1)) && (1146129076 == (*addrTmp2)))
				{
					_bloodAddr = ret + nDeltaBlood32;
					_crazyAddr = ret + nDeltaCrazy32;
					LOGE("+++update DadNMe(alternative) _bloodAddr _crazyAddr\n");
				}
			}
			else//�������γ���ʱ
			{
				//1065353216 1146129076
				_bloodAddr = ret + nDeltaBlood32;
				_crazyAddr = ret + nDeltaCrazy32;
				LOGE("+++update DadNMe _bloodAddr _crazyAddr: %x %x %d %d\n", _bloodAddr, _crazyAddr, 
				*(static_cast<unsigned int*>(_bloodAddr)), *(static_cast<unsigned int*>(_crazyAddr)));
				/*unsigned int* addrTmp1 = static_cast<unsigned int*>(_bloodAddr);
				unsigned int* addrTmp2 = static_cast<unsigned int*>(_crazyAddr);
				LOGE("value: %d %d\n", (int)(*addrTmp1), (int)(*addrTmp2));*/
			}
		}
		
�����е��жϣ�
if ((1065353216 == (*addrTmp1)) && (1146129076 == (*addrTmp2)))
��ͬ�ֻ�û���Թ���ֵ�ǲ�����ͬ
```