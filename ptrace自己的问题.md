#

```
 ptrace(PTRACE_TRACEME,0,NULL,NULL);
 ��������������
```

```
int keep_blood()
{
	if (0 == hookDadNMe::_curPid)
		return -1;
	if (nullptr == hookDadNMe::_bloodAddr)//_bloodAddr����������Χ���
		return -1;
	/*pid_t target_pid = hookDadNMe::_curPid;
	int status;
	LOGE("#########	attach %d %d %d\n", hookDadNMe::_curPid, find_pid_of("com.lakegame.dadnme"), target_pid);
	if (ptrace(PTRACE_ATTACH, target_pid, NULL, NULL) == -1L)//so ����app�У�so��app��һ�������У�����attachʧ�ܣ���֪���ǲ���д��������???
	//ȷ�ϸ��˽����Ǹ���rootȨ�޵ģ���MainActivity��OnCreate�����е����� Shell.isSuAvailable();
	//���������һ�����̣���rootȨ�ޣ�������Virual Xposed��ҹ��ģ�������ǿ���attach��
	{
		LOGE("failed to attach\n");
		LOGE("errno %s %d\n", strerror(errno), errno);//errno Operation not permitted 1
        return -1;
    }
	if (waitpid(target_pid, &status, 0) == -1 || !WIFSTOPPED(status))
	{
		LOGE("there was an error waiting for the target to stop.\n");
        return -1;
    }
	
	char buf[] = { 0x40, 0x51, 0x80, 0x00 };
	void *data = buf;
	

	long ptraced_long = ptrace(PTRACE_PEEKDATA, target_pid, hookDadNMe::_bloodAddr, NULL);
	if (1)
	{
		LOGE("ptraced_long	%d\n", ptraced_long);
	}

	if (ptrace(PTRACE_POKEDATA, target_pid, hookDadNMe::_bloodAddr, *(long *)(data)) == -1L)	
	{
		LOGE("memory allocation failed 1.\n");
		return -1;
    }

	LOGE("#########	detach\n");
	ptrace(PTRACE_DETACH, target_pid, 1, 0);*/
	//so��app��ͬһ�����̣���ʵ����ֱ�ӷ����ڴ�
	unsigned int* addr = static_cast<unsigned int*>(hookDadNMe::_bloodAddr);
	*addr = 1079083008;//0x405180000h;1079083008D;3.2734375F
	return 0;
}

```