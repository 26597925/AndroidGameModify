# ��װ

```
https://github.com/frida/frida
https://github.com/frida/frida/releases

https://frida.re/

https://blog.csdn.net/hujun5281/article/details/106516970/
https://blog.csdn.net/guo343310267/article/details/88343025


pip install frida-tools
��һ�����д�������һ������
������һ�ΰ�װ�ɹ���
```

```
adb forward tcp:27042 tcp:27042
adb forward tcp:27043 tcp:27043

demo
https://www.bilibili.com/video/BV1jJ411K7Xx/?spm_id_from=333.788.videocard.7
https://github.com/abcdsxg/frida-practice/tree/master/practice-1
��eclipseд�Ĺ���hookʧ���ˣ�Android Studio�Ĺ���hook�ɹ�
public class MainActivity extends AppCompatActivity {		Android Studio

public class MainActivity extends ActionBarActivity {		eclipse
```

```
Java��Hook(��ͨ���������췽�������ط������������������޸Ķ�������)
https://www.bilibili.com/video/BV1Z4411j7at/?p=3
https://www.bilibili.com/video/BV1Ei4y1b7ST	��ӡJava�㺯����ջ��λ�ؼ�����

YouTube�̳� Android����---Hook���������Frida����ʹ�����
https://www.bilibili.com/video/BV1yE411f7uW/?spm_id_from=333.788.videocard.11
```

```
Frida hook native�еĺ���
https://www.jianshu.com/p/b833fba1bffe

�����԰���wp Level1 Writeupʹ��Frida hook�����ȡflag��

Fridaʹ�õĹ����в��ܺ�Magisk Hideһ��ʹ��, ��Ȼ�����Failed to spawn: unable to access zygote64 while preparing for app launch; try disabling Magisk Hide in case it is active�ı�������������Ҫ�ȹص�Magisk Hide(Magisk Manager > Settings >Magisk > Magisk Hide (�ص�)), ���һ�Ҫ��Frida�ű������ƹ�root�ļ�⡣

ipython
https://blog.csdn.net/qq_39362996/article/details/82892671
```

```
frida objection ZenTracer
https://www.anquanke.com/post/id/197657

objection�İ�װ��
pip3 install objection

objectionע�롰���á�Ӧ��
	objection -g com.android.settings explore
�鿴�ڴ��м��صĿ�
	memory list modules
�鿴��ĵ�������
	memory list exports libssl.so
��������浽json�ļ���
	 memory list exports libart.so --json c:\\libart.json 

����û��hook so??
```

```
FRIDAϵ������
https://github.com/r0ysue/AndroidSecurityStudy
```

```
frida doc
https://frida.re/docs/

frida�����޷�attach /data/local/tmp����������elf����
  printf("pid: %d\n", getpid());
  printf ("f() is at %p\n", f);
  session = frida.attach(30434)
����pid ȥattach��ʧ�ܣ�adb shell ps > msg.txt �鿴�������̺�

Interceptor NativePointer(Function/Callback)ʹ��
https://www.anquanke.com/post/id/195869#h3-16
```

```
ʹ��frida���hook so�����ӣ�������ӡ��������������ֵ���޸ķ���ֵ
hook����chrom����� com.android.chrome
����ʱ open.py pid

import frida
import sys
import io

device = frida.get_usb_device()

session = device.attach(int(sys.argv[1]))

scr = """
setImmediate(function() {
Interceptor.attach(Module.findExportByName("libc.so" , "open"), {
    onEnter: function(args) {

        send("open called! args[0]:",Memory.readByteArray(args[0],256));		��libc.so��open�����ĵ�һ�������浽�ļ�D:\\log.txt��
		console.log('args[1]  : ' + args[1].toInt32());							��ӡlibc.so��open�����ĵڶ�������
    },
    onLeave:function(retval){
		console.log('retval  :' + retval.toInt32());
		retval.replace(666);													�޸�libc.so��open�����ķ���ֵ
		console.log('retval replace :' + retval.toInt32());						ע��������޸ķ���ֵ�п��ܵ���attach�Ľ��̱���
    }
});

});
"""

def on_message(message ,data):
    file_object=open("D:\\log.txt",'ab+')
    file_object.write(message['payload'].encode())
    file_object.write(data.split(b'\x00')[0])
    file_object.write('\n'.encode())
    file_object.close()


script = session.create_script(scr)
script.on("message" , on_message)
script.load()
sys.stdin.read()
```

```
ʹ��frida���hook so�����ӣ�����replace����
hook����chrom����� com.android.chrome
����ʱ openReplace.py pid

import frida
import sys
import io


device = frida.get_usb_device()

session = device.attach(int(sys.argv[1]))

scr = """
setImmediate(function() {
	var open_method = new NativeFunction(Module.findExportByName('libc.so', 'open'), 'int',['pointer','int']);
	 Interceptor.replace(open_method, new NativeCallback(function (a, b) {
            return -1;															hook��libc.so��open������ֱ�ӷ���-1
       }, 'int', ['pointer', 'int']));
});
"""

def on_message(message ,data):
   print('on_message')


script = session.create_script(scr)
script.on("message" , on_message)
script.load()
sys.stdin.read()


��openReplace.py pid
��open.py pid
�ῴ������open����֮��ĵķ���ֵ����-1
```

