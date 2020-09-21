# ����
```
������ȡ�˶�jni�����а�����
java�˵���System.loadLibrary()��
1��dlopen so
2��dlsym so�е�JNI_OnLoad���������ҵ���JNI_OnLoad����
3�����JNI_OnLoad��������registerNatives���Ա��ط�������ע�ᣬ�����ǲ������dlsym�ģ���Ϊ�ǽ�����ָ�뱣��������
https://blog.csdn.net/Saintyyu/article/details/90452826
4�������Java_com.xxxx_fun��jni�������ڵ���jni����ʱ��vm��dlysm jni��������ȡ��jni������ַ���ڵ���jni������ֻ��dlsymһ�Σ�
��Ϊ��ȡ��jni�����ĵ�ַ�󣬾Ͳ�����dlsym��

������registerNatives�ķ�ʽ����Java_com.xxxx_fun�ķ�ʽҪ��

https://www.jianshu.com/p/5252b62aa9d2


```

# registerNatives
```
JNINativeMethod nm;
nm.name = "g";
/* method descriptor assigned to signature field */
nm.signature = "()V";
nm.fnPtr = g_impl;
(*env)->RegisterNatives(env, cls, &nm, 1);

fnPtr�Ǻ����ĵ�ַ��������RegistetNativesע���ı��ط����ǲ���ȥ����dlsym��


ע�������ֵ��ȡ��ַ����ȡ�����ĵ�ַ
System.c
/* Only register the performance-critical methods */
static JNINativeMethod methods[] = {
    {"currentTimeMillis", "()J",              (void *)&JVM_CurrentTimeMillis},
    {"nanoTime",          "()J",              (void *)&JVM_NanoTime},
    {"arraycopy",     "(" OBJ "I" OBJ "II)V", (void *)&JVM_ArrayCopy},
};

#undef OBJ

JNIEXPORT void JNICALL
Java_java_lang_System_registerNatives(JNIEnv *env, jclass cls)
{
    // ע�᱾�ط���
    (*env)->RegisterNatives(env, cls,
                            methods, sizeof(methods)/sizeof(methods[0]));
}
```

# frida hook registerNatives���� 
```
Java.perform(function(){
        var envAddr = ptr(Java.vm.tryGetEnv().handle).readPointer();
        var registerNativesAddr = envAddr.add(860).readPointer();//32λ��so 216*4 - 4 = 860�� 64λ��so 216*8 - 8 = 1720
        console.log("registerNativesAddr", registerNativesAddr)
        if(registerNativesAddr != null){     													//Hook registerNatives ��ȡ��̬ע��ĺ�����ַ
			console.log("Interceptor.attach registerNatives")
            Interceptor.attach(registerNativesAddr,{
                onEnter: function(args){
                    console.log("registerNatives---begin")
					console.log(args[2].readPointer().readCString());							//��ӡ������name
					console.log(args[2].add(Process.pointerSize).readPointer().readCString());	//��ӡ
					console.log(args[2].add(Process.pointerSize * 2).readPointer());			//��ӡ�����ĵ�ַ
                },
                onLeave: function(retval){
					console.log("registerNatives---end  \\n\\n")
                }
            });
        }

    });

����registerNatives�ĵ�ַ�ǻ���envȥ��ƫ�Ƶ�
�鿴 jni.h��struct JNINativeInterface {	
����ı�������ָ�����ͣ�ֻ���ҵ�registerNatives��ƫ�Ƽ��ɣ�������216 -1
	//32λ��so 216*4 - 4 = 860�� 64λ��so 216*8 - 8 = 1720
	
������IDA��so���鿴JNI_OnLoad��registerNatives����ƫ�Ƶ�ֵ
signed int __fastcall sub_DDC(int a1, int a2, int a3, int a4)
{
  int v4; // ST08_4
  int v7; // [sp+0h] [bp-1Ch]
  int v8; // [sp+4h] [bp-18h]
  int v9; // [sp+Ch] [bp-10h]
  int v10; // [sp+14h] [bp-8h]

  v9 = a1;
  v4 = a2;
  v8 = a3;
  v7 = a4;
  _android_log_print(6, "testDlsym", "111111111111");
  v10 = (*(int (__fastcall **)(int, int))(*(_DWORD *)v9 + 24))(v9, v4);
  _android_log_print(6, "testDlsym", "22222222222");
  if ( !v10 )
    return 0;
  _android_log_print(6, "testDlsym", "33333333333");
  if ( (*(int (__fastcall **)(int, int, int, int))(*(_DWORD *)v9 + 860))(v9, v10, v8, v7) < 0 )			//�����ƫ����860�� v9��env�ĵ�ַ
    return 0;
  _android_log_print(6, "testDlsym", "44444444");
  return 1;
}
```

# ����
```
��ѩ�Ͽ���һƪ���£��ڲ��ø�smali�����´��������£�ʵ��hook
��������������Ƕ����пǻ��߷����Ե�apk�������Ϳ��Լ򵥵�ʵ��hook��
������߳�������ʹ��С���������Ϸ��ʧ���ˣ����Ƕ�jni�����̸���������
https://bbs.pediy.com/thread-261844.htm

```


# �鵽��һЩ��
```
1���鵽��
System.loadLibrary(libName)
->Runtime.loadLibrary(libName,classLoader)
->Runtime.doLoad(libName,loader)
->Runtime.nativeLoad(name,loader,ldLibraryPath)
->JavaVMExt.loadNativieLibrary:(JavaVMExt* vm=Runtime::Current()->GetJavaVM();vm->LoadNativieLibrary(filename,classloader,detail))
->jni_internal.cc::LoadNativieLibrary->dlopen,dlsym
->JNI_OnLoad


2���鵽��
System.loadLibrary(libName);
|--Runtime.loadLibrary0(libName,classLoader);
|--|--|--Runtime.nativeLoad(name,loader,ldLibraryPath);
|--|--|--Runtime_nativeLoad(JNIEnv* env, jclass, jstring javaFilename, jobject javaLoader, jstring javaLdLibraryPath);
|--|--|--|--JVM_NativeLoad(env, javaFilename, javaLoader);
|--|--|--|--JavaVMExt::LoadNativeLibrary(const std::string& path,Handle<mirror::ClassLoader> class_loader,std::string* detail)		
|--|--|--|--|--android::OpenNativeLibrary(dlopen);
|--|--|--|--|--|--SharedLibrary.FindSymbol;
|--|--|--|--|--|--SharedLibrary.FindSymbolWithoutNativeBridge(dlsym);

3���鵽��
./art/runtime/java_vm_ext.cc��
bool JavaVMExt::LoadNativeLibrary(JNIEnv* env,  
                                  const std::string& path,  
                                  jobject class_loader,  
                                  jstring library_path,  
                                  std::string* error_msg) 
{  
			......					  
	// Below we dlopen but there is no paired dlclose, this would be necessary if we supported  
    // class unloading. Libraries will only be unloaded when the reference count (incremented by  
    // dlopen) becomes zero from dlclose.  							  
								  
	void* handle = android::OpenNativeLibrary(env,  
                                            runtime_->GetTargetSdkVersion(),  
                                            path_str,  
                                            class_loader,  
                                            library_path);  
   
	bool needs_native_bridge = false;  
	if (handle == nullptr) {  
	if (android::NativeBridgeIsSupported(path_str)) {  												tag1	�˺�����������	dlopen �� dlsym
		handle = android::NativeBridgeLoadLibrary(path_str, RTLD_NOW);  
		needs_native_bridge = true;  
	}  
	}  
	
	VLOG(jni) << "[Call to dlopen(\"" << path << "\", RTLD_NOW) returned " << handle << "]";  
	
	if (handle == nullptr) {  
	*error_msg = dlerror();  
	VLOG(jni) << "dlopen(\"" << path << "\", RTLD_NOW) failed: " << *error_msg;  
	return false;  
	}  			

	sym = library->FindSymbol("JNI_OnLoad", nullptr);  												tag2	�ҵ�	JNI_OnLoad (Ӧ������dlsym�ҵ���)
	
	VLOG(jni) << "[Calling JNI_OnLoad in \"" << path << "\"]";  
    typedef int (*JNI_OnLoadFn)(JavaVM*, void*);  
    JNI_OnLoadFn jni_on_load = reinterpret_cast<JNI_OnLoadFn>(sym);  
    int version = (*jni_on_load)(this, nullptr);  													tag3	����	JNI_OnLoad
	
	...
}


4����so��JNI_OnLoad�����д�ӡ���Ķ�ջ
��ӡ�����Ķ�ջ
    backtrace:
    #00 pc 00004acd  /data/app/com.lakegame.dadnme-Dqh5EZjAUob4iJUGwNR5QA==/lib/arm/libCocos.so (_Z13callstackDumpRSs+00)
    #01 pc 00004b89  /data/app/com.lakegame.dadnme-Dqh5EZjAUob4iJUGwNR5QA==/lib/arm/libCocos.so (_Z15callstackLogcatiPKc+00)
    #02 pc 00004fad  /data/app/com.lakegame.dadnme-Dqh5EZjAUob4iJUGwNR5QA==/lib/arm/libCocos.so (JNI_OnLoad+00)
    #03 pc 0028ee35  /apex/com.android.runtime/lib/libart.so (_ZN3art9JavaVMExt17LoadNativeLibraryEP7_JNIEnvRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEP8_jobjectP7_jclassPS9_+00)
    #04 pc 000039a3  /apex/com.android.runtime/lib/libopenjdkjvm.so (JVM_NativeLoad+00)
	
���ۣ�
java��System.loadLibrary so֮�󣬴�JavaVMExt::LoadNativeLibrary�������Կ��������ȵ���dlopen dlsym��Ȼ���ڽ���so��JNI_OnLoad������
ע�����������
	// Below we dlopen but there is no paired dlclose, this would be necessary if we supported  
    // class unloading. Libraries will only be unloaded when the reference count (incremented by  
    // dlopen) becomes zero from dlclose.  	
������JNI_OnLoad�����������dlopen ��so�����صľ������һ����

```