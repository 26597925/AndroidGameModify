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