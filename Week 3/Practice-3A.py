{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The offered rates ...chose a one of them : **************************************************************************************************** {'USDAED': 3.673042, 'USDAFN': 75.000368, 'USDALL': 109.903989, 'USDAMD': 486.850403, 'USDANG': 1.774704, 'USDAOA': 309.351504, 'USDARS': 35.485041, 'USDAUD': 1.389104, 'USDAWG': 1.8, 'USDAZN': 1.702504, 'USDBAM': 1.594104, 'USDBBD': 2.0003, 'USDBDT': 83.844041, 'USDBGN': 1.717041, 'USDBHD': 0.376945, 'USDBIF': 1815, 'USDBMD': 1, 'USDBND': 1.458041, 'USDBOB': 6.92875, 'USDBRL': 3.696304, 'USDBSD': 0.99975, 'USDBTC': 0.000157, 'USDBTN': 72.915918, 'USDBWP': 10.670398, 'USDBYN': 2.119104, 'USDBYR': 19600, 'USDBZD': 2.00965, 'USDCAD': 1.310125, 'USDCDF': 1611.000362, 'USDCHF': 1.003404, 'USDCLF': 0.025048, 'USDCLP': 685.803912, 'USDCNY': 6.890904, 'USDCOP': 3177.95, 'USDCRC': 612.890395, 'USDCUC': 1, 'USDCUP': 26.5, 'USDCVE': 97.237504, 'USDCZK': 22.663604, 'USDDJF': 177.720394, 'USDDKK': 6.550804, 'USDDOP': 49.80504, 'USDDZD': 118.440393, 'USDEGP': 17.90804, 'USDERN': 15.000358, 'USDETB': 28.110392, 'USDEUR': 0.87817, 'USDFJD': 2.136504, 'USDFKP': 0.76999, 'USDGBP': 0.771125, 'USDGEL': 2.720391, 'USDGGP': 0.771091, 'USDGHS': 4.841304, 'USDGIP': 0.76999, 'USDGMD': 49.46504, 'USDGNF': 9125.000355, 'USDGTQ': 7.723704, 'USDGYD': 208.78504, 'USDHKD': 7.81705, 'USDHNL': 24.23504, 'USDHRK': 6.530204, 'USDHTG': 72.192504, 'USDHUF': 282.520388, 'USDIDR': 14925.55, 'USDILS': 3.695604, 'USDIMP': 0.771091, 'USDINR': 73.090387, 'USDIQD': 1190, 'USDIRR': 42105.000352, 'USDISK': 121.440386, 'USDJEP': 0.771091, 'USDJMD': 128.180386, 'USDJOD': 0.709504, 'USDJPY': 113.20404, 'USDKES': 101.40204, 'USDKGS': 69.758704, 'USDKHR': 4045.000351, 'USDKMF': 432.650384, 'USDKPW': 900.095821, 'USDKRW': 1118.130384, 'USDKWD': 0.30352, 'USDKYD': 0.83318, 'USDKZT': 371.020383, 'USDLAK': 8550.000349, 'USDLBP': 1514.950382, 'USDLKR': 172.220382, 'USDLRD': 157.375039, 'USDLSL': 14.390382, 'USDLTL': 2.95274, 'USDLVL': 0.60489, 'USDLYD': 1.395039, 'USDMAD': 9.516804, 'USDMDL': 17.134504, 'USDMGA': 3525.000347, 'USDMKD': 53.897039, 'USDMMK': 1602.25038, 'USDMNT': 2559.521726, 'USDMOP': 8.057404, 'USDMRO': 357.000346, 'USDMUR': 34.798039, 'USDMVR': 15.460378, 'USDMWK': 727.275039, 'USDMXN': 20.025804, 'USDMYR': 4.162504, 'USDMZN': 60.755039, 'USDNAD': 14.390377, 'USDNGN': 363.000344, 'USDNIO': 32.250377, 'USDNOK': 8.36765, 'USDNPR': 115.885039, 'USDNZD': 1.504535, 'USDOMR': 0.38506, 'USDPAB': 0.99985, 'USDPEN': 3.360375, 'USDPGK': 3.25215, 'USDPHP': 53.305039, 'USDPKR': 133.350375, 'USDPLN': 3.78325, 'USDPYG': 5993.450374, 'USDQAR': 3.641038, 'USDRON': 4.090104, 'USDRSD': 103.940373, 'USDRUB': 66.158104, 'USDRWF': 875, 'USDSAR': 3.749704, 'USDSBD': 8.237304, 'USDSCR': 13.641038, 'USDSDG': 47.602504, 'USDSEK': 9.06233, 'USDSGD': 1.375038, 'USDSHP': 1.320904, 'USDSLL': 8400.000339, 'USDSOS': 580.000338, 'USDSRD': 7.458038, 'USDSTD': 21050.59961, 'USDSVC': 8.74855, 'USDSYP': 515.000338, 'USDSZL': 14.39037, 'USDTHB': 32.84037, 'USDTJS': 9.42285, 'USDTMT': 3.5, 'USDTND': 2.886904, 'USDTOP': 2.274604, 'USDTRY': 5.429604, 'USDTTD': 6.73875, 'USDTWD': 30.604504, 'USDTZS': 2290.903635, 'USDUAH': 28.171038, 'USDUGX': 3742.703631, 'USDUSD': 1, 'USDUYU': 32.740367, 'USDUZS': 8226.000335, 'USDVEF': 248519.950366, 'USDVND': 23342, 'USDVUV': 114.855043, 'USDWST': 2.627825, 'USDXAF': 572.970365, 'USDXAG': 0.067817, 'USDXAU': 0.000811, 'USDXCD': 2.70255, 'USDXDR': 0.720674, 'USDXOF': 580.000332, 'USDXPF': 105.3036, 'USDYER': 250.350364, 'USDZAR': 14.304404, 'USDZMK': 9001.203593, 'USDZMW': 11.853037, 'USDZWL': 322.355011}\n"
     ]
    }
   ],
   "source": [
    "import requests as rq\n",
    "req1 = rq.get(\"http://apilayer.net/api/live?access_key=5958f554b1508888fa1275f492fd41d8\").json()\n",
    "\n",
    "print(\"The offered rates ...chose a one of them :\",100 * \"*\",req1[\"quotes\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the name:USDYER\n",
      "amout=100\n",
      "25035.0364 USD\n"
     ]
    }
   ],
   "source": [
    "a = input(\"enter the name:\")\n",
    "b = float(input (\"amout=\"))\n",
    "x = float(req1[\"quotes\"][a])\n",
    "print( x*b, \"USD\" )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
