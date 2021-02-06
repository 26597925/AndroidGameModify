#ifndef _timestamp_hpp_
#define _timestamp_hpp_

#include<chrono>
using namespace std::chrono;


class CTimestamp
{
public:
	CTimestamp()
	{
		update();
	}
	~CTimestamp()
	{}

	void    update()
	{
		_begin = high_resolution_clock::now();
	}
	/**
	*   ��ȡ��ǰ��
	*/
	double getElapsedSecond()
	{
		return  getElapsedTimeInMicroSec() * 0.000001;
	}
	/**
	*   ��ȡ����
	*/
	double getElapsedTimeInMilliSec()
	{
		return this->getElapsedTimeInMicroSec() * 0.001;
	}
	/**
	*   ��ȡ΢��
	*/
	long long getElapsedTimeInMicroSec()
	{
		return duration_cast<microseconds>(high_resolution_clock::now() - _begin).count();
	}
protected:
	time_point<high_resolution_clock> _begin;
};

#endif