#

```
sadls0122g �Ͱ汾�� ֻ����ģ���������� ���޸���
gtasa �°汾 �ڰ�׿10���޷����� �����޸���

���޸�����apk������libcleo.so��Ӧ����cheat menu�Ŀ�
libGTASA.so������һ��cheat�࣬GetPad������cheat

�����Գ���:ʥ������˹ ��׿�� ���������뷽���̳�		�Թ�������
https://www.jb51.net/gonglue/124541.html


```

#
```
����gg����Ҵ�cheat�˵��İ���
1����ȡ�����Գ��ֵĺ��Ӱ���assetsĿ¼����plugin-gta.apk��cheat�˵���nativeDoCheat(int i, int i2, int i3)��cheat���صĺ���
����i��Nativeid��i2��type, i3�ǿ��أ�Nativeid��type����Function���list��
2������plugin-gta.apk�е�libpgod.so��JNI_OnLoad/sub_1D8C/sub_22FC ��dlsym����ĺ�����
_ZN6CCheat11HealthCheatEv ... ����CCheat��ĺ���
"_ZN6CTimer6UpdateEv"
"_Z20SCSetCurrentLangaugePKc"
"_Z16AND_DeviceLocalev"

3������libpgod.so��jniDoProcessCheat����
����ǰ��Nativeid��type��switch case
��������һ��cheat��CCheat::SuicideCheat ���⣺���ĸ��������°���ǲ��������ģ��ϰ����Ϸapk��ȡʧ��

          case 8:
            result = dword_6084(1, 2057270476, 1074733655, 23);
            break;

.data.rel.ro.local:00005CD4                 DCD dword_6084
.data.rel.ro.local:00005CD8                 DCD aZn6ccheat12sui     ; "_ZN6CCheat12SuicideCheatEv"


.bss:00006084 ; int (__fastcall *dword_6084)(_DWORD, _DWORD, _DWORD, _DWORD)
.bss:00006084 dword_6084      % 4                     ; DATA XREF: sub_1974+218��r
.bss:00006084                                         ; .data.rel.ro.local:00005CD4��o

```

# �ƽ�˼·
```
�����Ƕ���Ϸ��ע�룬д�Ĵ�������so��ע�뵽��Ϸ����
���ֱ�ӽ�д��so�����Ϸ�����棬��java��loadLibrary���Ͳ���ע��so��
��GTASA.smali�����
    const-string v0, "inlineHook"
    invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V
	
��libGTASA.so�еĺ�������inline hook������ʵ��replace����

�����ǹؼ��㣺������������������������������������������������
�鿴libCEO.so
signed int __fastcall JNI_OnLoad(int a1)
int sub_51BC()
int __fastcall sub_46DC(int a1, int a2)
�����л�dlsym libGTASA.so�еĺ������鿴����
�о�_ZN14CRunningScript17ProcessOneCommandEv�е���ʹ��cheat�ĺ���

hook replace libGTASA.so�е�ProcessOneCommand������	hook replace���ɹ��ˣ�������Ϸ������
CRunningScript::ProcessOneCommand
�����鿴����
int __fastcall CRunningScript::Process(CRunningScript *this)
int __fastcall CGame::Process(CGame *this)

�о�CGame::Process�Ƚ�����Ϸ��ÿһ֡�ĺ���
hook replace ����CGame::Process����replace�����д�ӡ��־�����ֽ�����Ϸ�����󣬻᲻ͣ�����
int __fastcall CGame::Process(CGame *this)


�ں���CGame::Process��replace�����У�����f__ZN6CCheat12WeaponCheat1Ev��WeaponCheat1����Ч��

���ֱ�ӵ���WeaponCheat1��Ϸ�ǻ�����ģ�����Ӧ��������Ϸ��֡��֮֡��
```