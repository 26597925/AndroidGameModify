#˵��

```
�ο�
https://blog.csdn.net/taohongtaohuyiwei/article/details/105147933

Application.mk��APP_STL���ó�gnustl_static����ȻUnwind��صı��벻ͨ��
#APP_STL := stlport_static
APP_STL := gnustl_static
```

```
libCLEO.so����ĵ��ö�ջû�д�ӡ��ԭ�򣿣���

    backtrace:
    #00 pc 00004c15  /data/app/com.rockstargames.gtasa-DU1TjY3-wT5Qq_L9Tw88pQ==/lib/arm/libinlineHook.so (_Z13callstackDumpRSs+00)
    #01 pc 00004cd1  /data/app/com.rockstargames.gtasa-DU1TjY3-wT5Qq_L9Tw88pQ==/lib/arm/libinlineHook.so (_Z15callstackLogcatiPKc+00)
    #02 pc 00004d1d  /data/app/com.rockstargames.gtasa-DU1TjY3-wT5Qq_L9Tw88pQ==/lib/arm/libinlineHook.so (_Z19replaceWeaponCheat1Pv+00)
    #03 pc 00007ecf  /data/app/com.rockstargames.gtasa-DU1TjY3-wT5Qq_L9Tw88pQ==/lib/arm/libCLEO.so
```