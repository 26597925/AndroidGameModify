# �������public��Ա����
```
public class FighterMain extends BaseGameSprite
   {
		public var qi:Number = 0;
		
as���룺
 qi = 300;
 
pcode:
pushdouble 300.0
findproperty Qname(PackageNamespace(""),"qi")
swap
setproperty Qname(PackageNamespace(""),"qi")
```

#�������private��Ա����
```
public class FighterMain extends BaseGameSprite
   {
		private var _speedBack:Number = 0;
		
as���룺
 _speedBack = 300;
 
pcode:
pushdouble 300.0
findproperty Qname(PrivateNamespace("net.play5d.game.bvn.fighter:FighterMain"),"_speedBack")
swap
setproperty Qname(PrivateNamespace("net.play5d.game.bvn.fighter:FighterMain"),"_speedBack")
```

# ȡ���private��Ա����
```
public class BaseGameSprite extends EventDispatcher implements IGameSprite
   {
		private var _team:TeamVO;
		
public class TeamVO
   {
      public var id:int;
   
as���룺
var _loc2_:int = 0;
         _loc2_ = _team.id;
         if(_loc2_ == 1)
         {
            qi = 300;
            _speedBack = 300;
         }
		 
pcode:
		 
pushbyte 0
setlocal 2
getlex Qname(PrivateNamespace("net.play5d.game.bvn.interfaces:BaseGameSprite"),"_team")
getproperty Qname(PackageNamespace(""),"id")
convert_i
setlocal 2
getlocal 2
pushbyte 1
ifne ofs002b
ofs002b:
```

# ����FighterMain�� renderAnimate ����������_speedBack��Ϊteam.id
```
��������_speedBack����û�б�ʹ��
renderAnimateһֱ�ڵ���
team.id���ڴ�û�ҵ�ȷ�ϵķ���
�浽_speedBack�����У�_speedBack������Ѫ�ĵ�ַƫ����0xF4
```
