#
```
int main(int argc, char** argv)
{
	static char ori_buf1[] = { 0x01, 0xAD, 0x52, 0xE1 };//���ֽ�-->���ֽ� 0xE1 0x52 0xAD 0x01
	long *dataTest;
	dataTest = reinterpret_cast<long*>(ori_buf1);//dataTest��ֵ�� -514675455
	
	return 0;
}
```

#
```
��GG�޸�����ȡ�ĵ�ַ0x9D51CE40�������ֽ�������						E5802020
																			��E5802020�����ַ�����β��һ���ֽڵ�������20
arm�õ�С��ģʽ����β�ˣ�β�˵����ݴ���ڵ͵�ַ�����͵�ַ-->�ߵ�ַ	20 20 80 E5

�������ַ0x9D51CE40�������ֽ����� E5802020 ����һ�����ֽڵ�����
char buf[] = { 0x20, 0x20, 0x80, 0xE5 };
long lb = reinterpret_cast<long*>(buf);//lb��ֵ�� -444588000

```