# data-eng

Project contains data about Battery Charging and Discharging. The source data is huge to be uploaded onto this repository. Please feel free to connect to the author for the original source data.

Data Consists of :
- Battery Charging and Discharging process where details about
- current, voltage, capacitance, energy consumed and dissipated are all captured by IOT sensors in Real-time and Absolute time at the rate of 1 sample/second
- data is captured at each and every step of various cycles moitored at each jump

Project consists the task of:
- Combining and storing all the relavant data into appropriate `'detail.csv'`, `'detailVol.csv'` and `'detailTemp.csv'` from the original 'data.xlsx' and 'data_1.xlsx'
- Downsampling the data from 1 sample/second to 1 sample/minute
- Low pass filtering for noise removal
- Profile Testing using `cProfile`
- Unit Testing on all functions for various test cases using `unittest`
- Check to maintain `PEP-8` coding style using `pylint`

``` 
pylint Task_1.py  

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```
```
- pylint Task_2.py  --disable=C0303,C0305,C0103,C0114,C0116,c0115 --max-line-length=240
************* Module Task_2
Task_2.py:9:0: R0903: Too few public methods (1/2) (too-few-public-methods)

------------------------------------------------------------------
Your code has been rated at 9.60/10 (previous run: 9.60/10, +0.00)
```
