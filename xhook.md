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

# ����ֱ�Ӵ��ļ��ж�ȡ ELF ��Ϣ��
```
���ԡ����Ҷ��ڸ�ʽ������˵�����ļ��������׵ķ�ʽ����Ϊ ELF ������ʱ��ԭ�����кܶ� section ����Ҫһֱ�������ڴ��У������ڼ�����֮��ʹ��ڴ��ж������������Խ�ʡ�������ڴ档���Ǵ�ʵ���ĽǶȳ���������ƽ̨�Ķ�̬�������ͼ���������������ô��������������Ϊ���ӵĸ��Ӷȵò���ʧ���������Ǵ��ڴ��ж�ȡ���� ELF ��Ϣ�Ϳ����ˣ����ļ�����������������ġ����⣬ĳЩϵͳ�� ELF �ļ���APP Ҳ��һ���з���Ȩ�ޡ�
```

# �������ַ�ľ�ȷ������ʲô��
```
�������Ѿ�ע�⵽�ģ�ǰ����� libtest.so ����ַ��ȡʱ��Ϊ�˼򻯸���ͱ��뷽�㣬���ˡ������������¡����ֲ�Ӧ�ó��ֵ�������ʽ������ hook ��˵����ȷ�Ļ���ַ���������ǣ�

�� maps ���ҵ��ҵ� offset Ϊ 0���� pathname ΪĿ�� ELF ���С�������е� start address Ϊ p0��
�ҳ� ELF �� PHT �е�һ������Ϊ PT_LOAD �� offset Ϊ 0 �� segment������� segment �������ڴ���Ե�ַ��p_vaddr��Ϊ p1��
p0 - p1 ��Ϊ�� ELF ��ǰ�Ļ���ַ��
��������� ELF ��һ�� PT_LOAD segment �� p_vaddr ���� 0��

���⣬֮����Ҫ�� maps ���� offset Ϊ 0 ���У�����Ϊ������ִ�� hook ֮ǰ��ϣ�����ڴ��е� ELF �ļ�ͷ����У�飬ȷ����ǰ��������һ����Ч�� ELF�������� ELF �ļ�ͷֻ�ܳ����� offset Ϊ 0 �� mmap ����

������ Android linker ��Դ����������load_bias���������ҵ��ܶ���ϸ��ע��˵����Ҳ���Բο� linker �ж� load_bias_ �����ĸ�ֵ�����߼���
```
