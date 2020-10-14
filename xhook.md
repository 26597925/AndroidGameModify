#
```
xhook:������ Android native PLT hook ����
xhook ֧�� armeabi, armeabi-v7a �� arm64-v8a��֧�� Android 4.0 (��) ���ϰ汾 (API level >= 14)��

https://zhuanlan.zhihu.com/p/36426206

```

```
���°�����readme
https://github.com/iqiyi/xHook/blob/master/docs/overview/android_plt_hook_overview.zh-CN.md

ʾ������
https://github.com/iqiyi/xHook/tree/master/docs/overview/code

xhook��Ŀ��ַ
https://github.com/iqiyi/xHook
```

```
�ܽ�һ�� xhook ��ִ�� PLT hook �����̣�

1���� maps����ȡ ELF ���ڴ��׵�ַ��start address����
2����֤ ELF ͷ��Ϣ��
3���� PHT ���ҵ�����Ϊ PT_LOAD �� offset Ϊ 0 �� segment������ ELF ����ַ��
4���� PHT ���ҵ�����Ϊ PT_DYNAMIC �� segment�����л�ȡ�� .dynamic section���� .dynamic section�л�ȡ�������� section ��Ӧ���ڴ��ַ��
5���� .dynstr section ���ҵ���Ҫ hook �� symbol ��Ӧ�� index ֵ��
6���������е� .relxxx section���ض�λ section�������� symbol index �� symbol type ��ƥ�������������ض�λ�ִ�� hook ������hook �������£�
	�� maps��ȷ�ϵ�ǰ hook ��ַ���ڴ����Ȩ�ޡ�
	���Ȩ�޲��ǿɶ�Ҳ��д������ mprotect �޸ķ���Ȩ��Ϊ�ɶ�Ҳ��д��
	������÷���Ҫ���ͱ��� hook ��ַ��ǰ��ֵ�����ڷ��ء�
	�� hook ��ַ��ֵ�滻Ϊ�µ�ֵ����ִ�� hook��
	���֮ǰ�� mprotect �޸Ĺ��ڴ����Ȩ�ޣ����ڻ�ԭ��֮ǰ��Ȩ�ޡ�
	��� hook ��ַ�����ڴ�ҳ�Ĵ�����ָ��档
```