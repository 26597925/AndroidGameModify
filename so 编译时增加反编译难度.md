#
```
1��������ʱ����־�����
#include <android/log.h>
#ifdef DEBUG
#define LOGE(...)  __android_log_print(ANDROID_LOG_ERROR,"inlinehook",__VA_ARGS__)
#else
#define LOGE(...)
#endif

2������ʱ���ط���
Android.mk���
LOCAL_CPPFLAGS := -fvisibility=hidden

```
