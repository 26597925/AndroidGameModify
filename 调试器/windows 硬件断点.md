# ʹ��GetThreadContext/SetThreadContext��üĴ�����Ϣ
```
ÿ���̶߳���һ�������Ļ��������������й��̵߳Ĵ󲿷���Ϣ�������߳�ջ�ĵ�ַ���̵߳�ǰ����ִ�е�ָ���ַ�ȡ�
�����Ļ��������ڼĴ����У�ϵͳ�����̵߳��ȵ�ʱ��ᷢ���������л���ʵ���Ͼ��ǽ�һ���̵߳������Ļ������浽�ڴ��У�
Ȼ����һ���̵߳������Ļ���װ��Ĵ�����

typedef struct _CONTEXT {

    DWORD ContextFlags;
    DWORD   Dr0;
    DWORD   Dr1;
    DWORD   Dr2;
    DWORD   Dr3;
    DWORD   Dr6;
    DWORD   Dr7;
    FLOATING_SAVE_AREA FloatSave;
    DWORD   SegGs;
    DWORD   SegFs;
    DWORD   SegEs;
    DWORD   SegDs;
    DWORD   Edi;
    DWORD   Esi;
    DWORD   Ebx;    
    DWORD   Edx;
    DWORD   Ecx;
    DWORD   Eax;
    DWORD   Ebp;    //ջ��
    DWORD   Eip;     //��һ��ִ��ָ��
    DWORD   SegCs;              // MUST BE SANITIZED
    DWORD   EFlags;             // MUST BE SANITIZED
    DWORD   Esp;   //ջ��
    DWORD   SegSs;  //SS
    BYTE    ExtendedRegisters[MAXIMUM_SUPPORTED_EXTENSION];

} CONTEXT;

��ȡĳ���̵߳������Ļ�����Ҫʹ��GetThreadContext����
����GetThreadContext����֮��CONTEXT�ṹ��Ӧ���ֶξͻᱻ��ֵ����ʱ�Ϳ�����������Ĵ�����ֵ�ˡ�

ʹ��SetThreadContextд��Ĵ���ֵ 
```

# Ӳ���ϵ��ʵ��
```
DRx���ԼĴ����ܹ���8������DRx0��DRx7��ÿ���Ĵ������������£�
��������DR0~DR3�����Ե�ַ�Ĵ�����������Ҫ���ӵĵ�ַ��������Ӳ���ϵ㣻
��������DR4~DR5��������δ�����������ã�
��������DR6�����ԼĴ�����״̬�Ĵ����������ĸ��Ĵ���������
��������DR7���������ĸ�DRx���õĶϵ㣬�ֲ�����ȫ�֣���д/ִ��/д�ϵ����ͣ��ϵ㳤��1/2/4/8,����Ϣ

void SetBits(DWORD_PTR& dw, int lowBit, int bits, int newValue)
{
    DWORD_PTR mask = (1 << bits) - 1; 
    dw = (dw & ~(mask << lowBit)) | (newValue << lowBit);
}

/*
��һ������HANDLE hThread��
HANDLE g_hThread = NULL;
STARTUPINFO si = { 0 };
si.cb = sizeof(si);
PROCESS_INFORMATION pi = { 0 };
	if (CreateProcess(
		szFilePath,
		NULL,
		NULL,
		NULL,
		FALSE,
		DEBUG_ONLY_THIS_PROCESS | CREATE_NEW_CONSOLE,//ע������Ĳ���
		NULL,
		NULL,
		&si,
		&pi) == FALSE) {
			MessageBox(NULL,L"CreateProcess failed",L"MZ",1);
			return;
	}

	g_hProcess = pi.hProcess;
	g_hThread = pi.hThread;

���ĸ�����void* s��
ULONG Address = 0;//�ֶ�����

����SetHardwareBreakpoint��
SetHardwareBreakpoint(g_hThread, HWBRK_TYPE_CODE, HWBRK_SIZE_1, (void*)Address);
*/
HANDLE SetHardwareBreakpoint(HANDLE hThread,HWBRK_TYPE Type,HWBRK_SIZE Size,void* s)
{ 
	...
	SuspendThread(hThread);
	
	//��ȡ�̵߳������Ļ���
	CONTEXT ct = {0};
	ct.ContextFlags = CONTEXT_DEBUG_REGISTERS|CONTEXT_FULL;
	GetThreadContext(hThread,&ct);
	
	//����HWBRK_TYPE Type,HWBRK_SIZE Sizeȷ��st le
	int st = 0;
	if (Type == HWBRK_TYPE_CODE)
        st = 0;
	int le = 0;
	if (Size == HWBRK_SIZE_1)
        le = 0;
	
	//���õ��ԼĴ���
	ct.Dr0 = (DWORD_PTR)s;  //��ַ
	ct.Dr6 = 0;
	SetBits(ct.Dr7, 16 + iReg*4, 2, st);
    SetBits(ct.Dr7, 18 + iReg*4, 2, le);
    SetBits(ct.Dr7, iReg*2,1,1);
	
	//�����̵߳������Ļ���
	ct.ContextFlags = CONTEXT_DEBUG_REGISTERS;
	SetThreadContext(hThread,&ct);
	
	ResumeThread(hThread);
	...
}
```

#����Ӳ���ϵ�
```
ContinueDebugSession(step in/out/over�ȸ��ֵ��Գ��������)
DispatchDebugEvent
OnException
OnSingleStep


void ContinueDebugSession() {
	while (WaitForDebugEvent(&debugEvent, INFINITE) == TRUE) {//ѭ��
		if (DispatchDebugEvent(&debugEvent) == TRUE) {

//���ݵ����¼������͵��ò�ͬ�Ĵ�������
BOOL DispatchDebugEvent(const DEBUG_EVENT* pDebugEvent) {
	switch (pDebugEvent->dwDebugEventCode) {
		case EXCEPTION_DEBUG_EVENT:
		{
			return OnException	(&pDebugEvent->u.Exception);
		}
	

//�����쳣��ʱ��Ӧ��֪ͨ�û��������û�����������Ӧ����FALSE��
BOOL OnException(const EXCEPTION_DEBUG_INFO* pInfo) {
	case EXCEPTION_BREAKPOINT:
		{
			/*OnShowSourceLines();*/
			
			return OnSoftBreakPoint(pInfo);   //return false ���ж�ͣ����
		}

	case EXCEPTION_SINGLE_STEP:  
		{
			/*OnShowSourceLines();*/
			
			return OnSingleStep(pInfo);
		}
}


BOOL OnSingleStep(const EXCEPTION_DEBUG_INFO* pInfo)������

	CONTEXT Context = {0};
	GetDebuggeeContext(&Context);
	for(DWORD i = 0; i < m_vecHard.size( ); ++i)
	{
		if(m_vecHard[i].lpPointAddr ==(DWORD)pInfo->ExceptionRecord.ExceptionAddress)
		{
			CString strStatusMsg;
			strStatusMsg.Format(L"A Hard break point occured at %p",(DWORD)pInfo->ExceptionRecord.ExceptionAddress);
	
	...
	
	
```



