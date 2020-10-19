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

# ELF
```
ELF��Executable and Linkable Format����һ����ҵ��׼�Ķ��������ݷ�װ��ʽ����Ҫ���ڷ�װ��ִ���ļ�����̬�⡢object �ļ��� core dumps �ļ���

ʹ�� google NDK ��Դ������б�������ӣ����ɵĶ�̬����ִ���ļ����� ELF ��ʽ�ġ��� readelf ���Բ鿴 ELF �ļ��Ļ�����Ϣ���� objdump ���Բ鿴 ELF �ļ��ķ���������
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

#hook ʱ����ż���Ķδ�����δ���
```
���������

�� hook �߼�����������Ϊ��Σ������ֱ�Ӽ����ڴ��ַ���ж�д��֮ǰ��ͨ��һ��ȫ�� flag �����б�ǣ��뿪Σ������� flag ��λ��
ע�������Լ��� signal handler��ֻ����δ����� signal handler �У�ͨ���ж� flag ��ֵ�����жϵ�ǰ�߳��߼��Ƿ���Σ�������С�����ǣ����� siglongjmp ���� signal handler��ֱ����������Ԥ�����úõġ�Σ�������������һ�д��봦����������ǣ��ͻָ�֮ǰ������������ע��� signal handler��Ȼ��ֱ�ӷ��أ���ʱϵͳ���ٴ������ǵ��̷߳��Ͷδ����źţ������Ѿ��ָ���֮ǰ�� signal handler����ʱ�����Ĭ�ϵ�ϵͳ signal handler ���������߼���
���ǰ����ֻ��Ƽ��Ϊ��SFP (segmentation fault protection���δ��󱣻�)
ע�⣺SFP��Ҫһ�����أ���������ʱ�ܹ������͹ر������� APP �������Խ׶Σ�SFP Ӧ��ʼ�ձ��رգ������Ͳ��������ڱ���ʧ���µĶδ�����Щ������Ӧ�ñ��޸��ģ�����ʽ���ߺ� SFP Ӧ�ñ������������ܱ�֤ APP �������������Ȼ���Բ�������ʽ���ֹر� SFP�����Թ۲�ͷ��� hook ���Ʊ����µı�����Ҳ�ǿ��Կ��ǵģ�
���������Բο� xhook �е�ʵ�֣���Դ�������� siglongjmp �� sigsetjmp��
```

# ELF �ڲ�����֮��ĵ����� xhook ��
```
����������ܵ� hook ��ʽΪ PLT hook�������� ELF �ڲ�����֮����õ� hook��

inline hook ��������������Ҫ��֪����Ҫ hook ���ڲ�������������symbol name�����ߵ�ַ��Ȼ����� hook��

�кܶ࿪Դ�ͷǿ�Դ�� inline hook ʵ�֣����磺

substrate��http://www.cydiasubstrate.com/
frida��https://www.frida.re/
inline hook ����ǿ���ͬʱ���ܴ������µ����⣺

������Ҫֱ�ӽ������޸� ELF �еĻ���ָ�����룩�����ڲ�ͬ�ܹ��Ĵ�������������ָ����������Ż�ѡ�����ϵͳ�汾���ܴ��ڲ�ͬ�ļ����Ժ��ȶ������⡣
���������������Է����Ͷ�λ��һЩ֪���� inline hook �����Ǳ�Դ�ġ�
ʵ��������Ը��ӣ��Ѷ�Ҳ�ϴ�
δ֪�Ŀ���Խ϶࣬����������� google��
������� PLT hook ���õĻ����Ͳ��س��� inline hook �ˡ�

```
