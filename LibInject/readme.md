# 

```
https://blog.csdn.net/h523669057/article/details/42876119
1���˴����������صģ�ֻ֧��32λ���̣������64λ����ע���ʧ�ܣ���Ϊ������ʹ����regs->ARM_pc

2��libc_path linker_path 
��/proc/uid/maps�ļ��п��Բ鿴��
const char *libc_path = "/apex/com.android.runtime/lib/bionic/libc.so";    
const char *linker_path = "/apex/com.android.runtime/lib/bionic/libdl.so";  

ԭ���Ĵ���̫�ϣ�
const char *libc_path = "/system/lib/libc.so";    
const char *linker_path = "/system/bin/linker"; 

3�����ݰ�����ȡ���̺�
pid_t target_pid = find_pid_of("com.and.games505.TerrariaPaid");    

4��ע��so��������
��push libhello.so��/data/local/tmpĿ¼�£�Ȼ�����adb shell ��su, cp libhello.so��/data/app/com.and.games505.TerrariaPaid-zEFfgdCC4F8y6CFw-m7lNw==/lib/arm/ ��
ע�������libhello.soҪ������/data/app/com.and.games505.TerrariaPaid-zEFfgdCC4F8y6CFw-m7lNw==/lib/arm/ ��
Ŀ¼�Ļ�ȡ�ǲ鿴/proc/uid/maps�ļ��е�����so��ŵ�Ŀ¼�����Ŀ¼��app��װ֮��Ͳ���ı��
cat /proc/19426/maps | grep libunity	����libunity.so��ŵ�Ŀ¼������Ҫ������Ŀ¼

inject_remote_process(target_pid, "libhello.so", "hook_entry",  "I'm parameter!", strlen("I'm parameter!"));  

ԭ���Ĵ����ǣ�
inject_remote_process(target_pid, "/data/libhello.so", "hook_entry",  "I'm parameter!", strlen("I'm parameter!"));    

```