# ����Ѫ ��Ӧ�ı��� hp�������� Number ռ��8���ֽڣ����Ե���double
```
package net.play5d.game.bvn.interfaces
	public class BaseGameSprite extends EventDispatcher implements IGameSprite
	
	public function loseHp(param1:Number) : void
      {
         if(!isAllowLoseHP)
         {
            return;
         }
         var _loc3_:* = Number(2 - defenseRate);
         if(_loc3_ < 0.1)
         {
            _loc3_ = 0.1;
         }
         if(_loc3_ > 1)
         {
            _loc3_ = 1;
         }
         var _loc2_:Number = param1 * _loc3_ - defense;
         if(_loc2_ < 0)
         {
            return;
         }
         hp = hp - _loc2_;
         if(hp < 0)
         {
            hp = 0;
         }
      }
team.id == 1ʱ��ֱ�Ӹ�ֵhpΪ1000���ڷ��أ�����ֱ�ӷ���
```

# ������	��Ӧ�ı��� energy�������� Number ռ��8���ֽڣ����Ե���double
```
package net.play5d.game.bvn.fighter
 public class FighterMain extends BaseGameSprite
 
    public function useEnergy(param1:Number) : void
      {
         energy = energy - param1;
         _energyAddGap = 0.8 * 30;
         if(energy < 0)
         {
            energy = 0;
            energyOverLoad = true;
         }
      }
team.id == 1ʱ��ֱ�Ӹ�ֵenergyΪ100���ڷ���
```

# ����sp	��Ӧ�ı��� qi�������� Number ռ��8���ֽڣ����Ե���double
```
package net.play5d.game.bvn.fighter
 public class FighterMain extends BaseGameSprite
 
      public function useQi(param1:Number) : Boolean
      {
         if(qi < param1)
         {
            return false;
         }
         qi = qi - param1;
         return true;
      }
team.id == 1ʱ��ֱ�Ӹ�ֵqiΪ300���ڷ���
```

# ���޸��� ��Ӧ�ı��� fzqi�������� Number ռ��8���ֽڣ����Ե���double
```
package net.play5d.game.bvn.fighter
 public class FighterMain extends BaseGameSprite
 
	private function renderFzQi() : void
      {
         if(fzqi < 100)
         {
            fzqi = fzqi + 0.2;
         }
      }
team.id == 1ʱ��ֱ�Ӹ�ֵfzqiΪ100���ڷ���
```