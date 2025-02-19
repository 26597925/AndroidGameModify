import frida
import sys
import io


device = frida.get_usb_device()

session = device.attach("com.xigmaGames.thebonfire2")

scr = """
function hookTest(){
    var soAddr = Module.findBaseAddress("libil2cpp.so");
    console.log(soAddr);

    var funcAddr = soAddr.add(0x5E5228); //函数地址计算 thumb+1 ARM不加	
    console.log(funcAddr);
	
	var count = 0;

    if(funcAddr != null){
		console.log("attach");
        Interceptor.attach(funcAddr,{
		
		
            onEnter: function(args){
				console.log("onEnter ---------------------------------<");
				//console.log(Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\\n') + '\\n');
				console.log(args[0]);
				//console.log(args[1]);
				console.log(hexdump(args[0].add(0x1C))); //智力
				//console.log(hexdump(args[0].add(0x20))); //经验
				//var intelligence = args[0].add(0x1C);
				//console.log(intelligence.toInt32);
            },
            onLeave: function(retval){
				//count = count +1;
				//console.log(retval.toInt32()*count);
				//retval.replace(retval.toInt32()*count*100);	
				//if (retval != 0)
                console.log("onLeave---------------------------------");
				//console.log(Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\\n') + '\\n');
				//console.log(retval);
				//console.log("onLeave--------------------------------->\\n");
				//console.log('retval  :' + retval.toInt32());
				//retval.replace(1557644296);													
				//console.log('retval replace :' + retval.toInt32());		
				//return retval;
            }
        });
     }
	
}

call_GetInstance(){
	var base_addr = Module.findBaseAddress("libil2cpp.so");
    var addr_fun_0x5D88D8 = base_addr.add(0x5D88D8);
    var sub_GetInstance = new NativeFunction(addr_fun_0x5D88D8, "int", []);
	console.log(sub_GetInstance());
}

function main(){
	hookTest();
}

setImmediate(main);
"""

def on_message(message ,data):
   print('on_message')


script = session.create_script(scr)
script.on("message" , on_message)
script.load()
sys.stdin.read()