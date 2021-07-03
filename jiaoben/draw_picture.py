#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:30:32 2020

@author: yangan
"""
import re
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

mystr='''
angleX : -31.03	angleY : 6.86	angleZ : -93.23angleX : -4.18	angleY : -16.59	angleZ : 100.22
angleX : -34.29	angleY : 10.55	angleZ : -66.84angleX : 13.99	angleY : 2.19	angleZ : 63.86
angleX : -51.90	angleY : 28.50	angleZ : -45.51angleX : 31.80	angleY : -7.78	angleZ : 46.77
angleX : -75.39	angleY : 29.80	angleZ : -34.64angleX : 30.51	angleY : -17.46	angleZ : 34.79
angleX : -87.82	angleY : 12.62	angleZ : -25.41angleX : 24.46	angleY : -28.37	angleZ : 21.80
angleX : -86.23	angleY : -5.29	angleZ : -19.17angleX : 21.65	angleY : -14.96	angleZ : 23.67
angleX : -75.53	angleY : -33.72	angleZ : -29.03angleX : 20.31	angleY : -0.51	angleZ : 42.73
angleX : -64.51	angleY : -46.86	angleZ : -48.76angleX : 21.03	angleY : 28.07	angleZ : 63.77
angleX : -50.06	angleY : -44.26	angleZ : -83.18angleX : 16.44	angleY : 64.98	angleZ : 88.68
angleX : -42.59	angleY : -25.76	angleZ : -113.69angleX : 56.17	angleY : 107.83	angleZ : 102.67
angleX : -37.09	angleY : -31.05	angleZ : -132.73angleX : 71.01	angleY : 143.79	angleZ : 121.08
angleX : -41.00	angleY : -12.93	angleZ : -135.71angleX : 76.74	angleY : 111.04	angleZ : 132.74
angleX : -34.71	angleY : -32.95	angleZ : -129.22angleX : 68.76	angleY : 90.09	angleZ : 128.01
angleX : -39.70	angleY : -18.06	angleZ : -119.60angleX : 68.28	angleY : 79.19	angleZ : 118.81
angleX : -39.90	angleY : -20.59	angleZ : -107.12angleX : 69.20	angleY : 57.62	angleZ : 113.87
angleX : -42.48	angleY : -12.98	angleZ : -100.98angleX : 62.22	angleY : 49.08	angleZ : 107.01
angleX : -45.51	angleY : -10.22	angleZ : -94.75angleX : 59.16	angleY : 48.07	angleZ : 102.58
angleX : -47.37	angleY : -10.66	angleZ : -88.56angleX : 66.72	angleY : 52.26	angleZ : 95.77
angleX : -49.41	angleY : -10.15	angleZ : -81.70angleX : 73.71	angleY : 59.40	angleZ : 85.12
angleX : -49.93	angleY : -9.19	angleZ : -75.46angleX : 75.14	angleY : 57.77	angleZ : 75.51
angleX : -50.02	angleY : -9.14	angleZ : -70.39angleX : 75.03	angleY : 47.97	angleZ : 67.18
angleX : -49.83	angleY : -13.58	angleZ : -64.71angleX : 70.85	angleY : 45.03	angleZ : 57.41
angleX : -49.93	angleY : -13.52	angleZ : -61.05angleX : 65.47	angleY : 31.56	angleZ : 45.60
angleX : -51.27	angleY : -10.77	angleZ : -60.40angleX : 60.50	angleY : -8.18	angleZ : 42.83
angleX : -51.99	angleY : -12.82	angleZ : -64.13angleX : 68.13	angleY : -8.73	angleZ : 69.47
angleX : -50.78	angleY : -39.50	angleZ : -83.08angleX : 69.21	angleY : 10.94	angleZ : 96.47
angleX : -50.74	angleY : -36.70	angleZ : -101.74angleX : 66.33	angleY : 18.95	angleZ : 119.93
angleX : -50.53	angleY : -35.94	angleZ : -116.35angleX : 54.05	angleY : 24.25	angleZ : 138.85
angleX : -50.47	angleY : -32.88	angleZ : -123.50angleX : 44.85	angleY : 44.32	angleZ : 158.41
angleX : -47.25	angleY : -37.75	angleZ : -126.34angleX : 39.80	angleY : 43.25	angleZ : 165.61
angleX : -41.49	angleY : -38.27	angleZ : -122.36angleX : 47.65	angleY : 26.50	angleZ : 145.97
angleX : -40.77	angleY : -27.31	angleZ : -109.81angleX : 56.07	angleY : 0.57	angleZ : 98.88
angleX : -49.44	angleY : -10.69	angleZ : -89.78angleX : 52.40	angleY : -46.76	angleZ : 50.87
angleX : -66.81	angleY : -9.80	angleZ : -73.00angleX : 61.32	angleY : -65.70	angleZ : 31.68
angleX : -88.46	angleY : -7.23	angleZ : -59.06angleX : 66.72	angleY : -55.41	angleZ : 24.67
angleX : -102.77	angleY : -6.08	angleZ : -47.99angleX : 77.65	angleY : -75.36	angleZ : 25.33
angleX : -112.32	angleY : -17.49	angleZ : -42.35angleX : 82.34	angleY : -82.34	angleZ : 29.78
angleX : -116.24	angleY : -24.50	angleZ : -42.70angleX : 85.76	angleY : -92.19	angleZ : 35.92
angleX : -109.05	angleY : -25.27	angleZ : -48.23angleX : 85.36	angleY : -106.92	angleZ : 43.71
angleX : -90.03	angleY : -27.65	angleZ : -65.15angleX : 70.67	angleY : -116.03	angleZ : 45.71
angleX : -74.05	angleY : -18.65	angleZ : -101.01angleX : 64.79	angleY : -112.81	angleZ : 65.00
angleX : -62.82	angleY : -7.09	angleZ : -137.62angleX : 73.63	angleY : -81.24	angleZ : 99.86
angleX : -59.24	angleY : -5.21	angleZ : -159.16angleX : 75.57	angleY : -41.23	angleZ : 140.37
angleX : -54.35	angleY : -21.01	angleZ : -163.04angleX : 65.40	angleY : -3.78	angleZ : 160.68
angleX : -52.52	angleY : -1.68	angleZ : -167.79angleX : 61.75	angleY : -9.97	angleZ : 160.07
angleX : -49.16	angleY : 5.03	angleZ : -162.84angleX : 67.64	angleY : -36.31	angleZ : 145.83
angleX : -52.69	angleY : 1.32	angleZ : -137.72angleX : 70.72	angleY : -48.10	angleZ : 121.06
angleX : -72.69	angleY : 30.01	angleZ : -107.85angleX : 79.57	angleY : -82.73	angleZ : 108.73
angleX : -98.72	angleY : 25.76	angleZ : -95.00angleX : 80.19	angleY : -104.15	angleZ : 89.07
angleX : -111.59	angleY : 8.34	angleZ : -79.78angleX : 73.29	angleY : -126.03	angleZ : 72.38
angleX : -115.95	angleY : -0.23	angleZ : -71.86angleX : 56.49	angleY : -116.16	angleZ : 53.81
angleX : -109.06	angleY : -6.46	angleZ : -76.70angleX : 56.58	angleY : -116.86	angleZ : 60.66
angleX : -97.64	angleY : -14.01	angleZ : -92.76angleX : 53.29	angleY : -104.87	angleZ : 76.04
angleX : -86.45	angleY : -23.83	angleZ : -130.63angleX : 59.27	angleY : -89.06	angleZ : 100.85
angleX : -76.05	angleY : -45.82	angleZ : -157.34angleX : 72.77	angleY : -68.68	angleZ : 137.10
angleX : -70.13	angleY : -46.13	angleZ : -185.92angleX : 75.91	angleY : -56.53	angleZ : 168.79
angleX : -69.89	angleY : -40.53	angleZ : -193.61angleX : 91.47	angleY : -49.41	angleZ : 178.45
angleX : -68.80	angleY : -34.40	angleZ : -184.60angleX : 112.88	angleY : -24.07	angleZ : 181.60
angleX : -67.88	angleY : -37.41	angleZ : -162.62angleX : 119.96	angleY : -21.87	angleZ : 181.55
angleX : -78.43	angleY : -38.21	angleZ : -125.96angleX : 109.91	angleY : -47.26	angleZ : 173.82
angleX : -94.55	angleY : -23.20	angleZ : -89.98angleX : 100.91	angleY : -64.66	angleZ : 159.66
angleX : -108.00	angleY : -27.01	angleZ : -70.39angleX : 94.74	angleY : -78.10	angleZ : 151.15
angleX : -116.98	angleY : -35.92	angleZ : -58.87angleX : 80.37	angleY : -96.61	angleZ : 131.83
angleX : -115.46	angleY : -45.17	angleZ : -61.74angleX : 73.52	angleY : -117.61	angleZ : 117.61
angleX : -105.10	angleY : -53.10	angleZ : -68.36angleX : 62.83	angleY : -114.51	angleZ : 108.30
angleX : -86.65	angleY : -57.84	angleZ : -90.29angleX : 61.43	angleY : -115.18	angleZ : 111.19
angleX : -73.23	angleY : -50.09	angleZ : -119.84angleX : 72.48	angleY : -101.03	angleZ : 124.42
angleX : -70.20	angleY : -51.46	angleZ : -154.75angleX : 85.10	angleY : -54.19	angleZ : 143.93
angleX : -73.39	angleY : -49.13	angleZ : -176.56angleX : 92.27	angleY : -19.88	angleZ : 166.18
angleX : -70.21	angleY : -33.29	angleZ : -192.33angleX : 92.71	angleY : 0.16	angleZ : 182.47
angleX : -60.32	angleY : -49.69	angleZ : -191.06angleX : 85.38	angleY : -5.49	angleZ : 186.55
angleX : -65.25	angleY : -38.51	angleZ : -175.57angleX : 82.71	angleY : -7.00	angleZ : 185.85
angleX : -77.32	angleY : -34.37	angleZ : -140.05angleX : 81.83	angleY : -32.86	angleZ : 180.21
angleX : -93.61	angleY : -16.58	angleZ : -110.55angleX : 75.71	angleY : -49.64	angleZ : 169.89
angleX : -105.14	angleY : -21.31	angleZ : -90.14angleX : 68.16	angleY : -58.58	angleZ : 157.99
angleX : -113.22	angleY : -30.17	angleZ : -76.83angleX : 53.75	angleY : -86.94	angleZ : 132.89
angleX : -109.89	angleY : -60.22	angleZ : -69.73angleX : 47.92	angleY : -103.08	angleZ : 90.63
angleX : -94.89	angleY : -87.54	angleZ : -73.70angleX : 28.00	angleY : -132.10	angleZ : 55.15
angleX : -88.89	angleY : -76.86	angleZ : -101.22angleX : 28.73	angleY : -103.33	angleZ : 74.67
angleX : -84.96	angleY : -74.50	angleZ : -134.53angleX : 35.16	angleY : -95.48	angleZ : 99.39
angleX : -88.61	angleY : -57.69	angleZ : -171.95angleX : 37.28	angleY : -87.74	angleZ : 104.46
angleX : -90.28	angleY : -49.27	angleZ : -195.86angleX : 21.36	angleY : -67.56	angleZ : 92.14
angleX : -93.73	angleY : -71.80	angleZ : -200.99angleX : 18.15	angleY : -76.35	angleZ : 129.53
angleX : -91.33	angleY : -69.59	angleZ : -208.52angleX : 27.76	angleY : -63.17	angleZ : 170.94
angleX : -89.55	angleY : -60.68	angleZ : -210.06angleX : 31.21	angleY : -44.58	angleZ : 187.98
angleX : -89.97	angleY : -53.90	angleZ : -202.84angleX : 32.55	angleY : -40.02	angleZ : 177.78
angleX : -96.88	angleY : -53.56	angleZ : -178.12angleX : 34.55	angleY : -58.56	angleZ : 140.66
angleX : -113.28	angleY : -52.41	angleZ : -141.40angleX : 41.26	angleY : -88.23	angleZ : 116.29
angleX : -134.38	angleY : -39.80	angleZ : -115.27angleX : 55.43	angleY : -86.34	angleZ : 113.85
angleX : -144.80	angleY : -52.65	angleZ : -105.24angleX : 58.81	angleY : -99.82	angleZ : 97.79
angleX : -153.71	angleY : -52.53	angleZ : -104.91angleX : 53.04	angleY : -107.15	angleZ : 88.98
angleX : -141.06	angleY : -62.63	angleZ : -108.37angleX : 43.31	angleY : -99.49	angleZ : 97.59
angleX : -117.44	angleY : -83.46	angleZ : -125.64angleX : 32.64	angleY : -105.94	angleZ : 104.28
angleX : -112.58	angleY : -86.55	angleZ : -168.75angleX : 30.44	angleY : -97.19	angleZ : 129.29
angleX : -114.98	angleY : -81.36	angleZ : -208.58angleX : 43.69	angleY : -63.69	angleZ : 171.07
angleX : -110.88	angleY : -95.61	angleZ : -232.59angleX : 57.38	angleY : -13.64	angleZ : 201.03
angleX : -109.41	angleY : -85.91	angleZ : -244.30angleX : 57.10	angleY : 12.65	angleZ : 213.45
angleX : -101.40	angleY : -96.77	angleZ : -236.84angleX : 59.41	angleY : -10.98	angleZ : 211.58
angleX : -98.70	angleY : -88.81	angleZ : -212.36angleX : 63.14	angleY : -31.15	angleZ : 188.26
angleX : -96.76	angleY : -96.23	angleZ : -168.50angleX : 62.53	angleY : -69.15	angleZ : 175.02
angleX : -101.59	angleY : -91.97	angleZ : -140.44angleX : 57.98	angleY : -79.14	angleZ : 151.90
angleX : -109.61	angleY : -100.12	angleZ : -118.02angleX : 54.41	angleY : -125.37	angleZ : 131.75
angleX : -114.69	angleY : -114.92	angleZ : -107.00angleX : 45.05	angleY : -129.19	angleZ : 123.01
angleX : -105.54	angleY : -135.87	angleZ : -115.27angleX : 41.44	angleY : -110.21	angleZ : 118.45
angleX : -92.29	angleY : -126.13	angleZ : -134.55angleX : 54.76	angleY : -75.24	angleZ : 100.24
angleX : -90.18	angleY : -118.51	angleZ : -172.14angleX : 66.37	angleY : -44.90	angleZ : 101.89
angleX : -90.05	angleY : -103.15	angleZ : -209.06angleX : 53.11	angleY : -20.86	angleZ : 118.06
angleX : -91.44	angleY : -91.11	angleZ : -225.47angleX : 45.61	angleY : 2.68	angleZ : 138.14
angleX : -89.18	angleY : -90.76	angleZ : -227.10angleX : 36.70	angleY : 5.48	angleZ : 151.44
angleX : -85.44	angleY : -87.20	angleZ : -220.91angleX : 29.48	angleY : -1.42	angleZ : 164.05
angleX : -87.48	angleY : -71.35	angleZ : -217.11angleX : 33.60	angleY : 2.96	angleZ : 163.29
angleX : -86.68	angleY : -71.19	angleZ : -206.61angleX : 41.01	angleY : -20.14	angleZ : 147.52
angleX : -90.76	angleY : -55.93	angleZ : -181.24angleX : 47.38	angleY : -47.30	angleZ : 136.14
angleX : -109.89	angleY : -65.01	angleZ : -159.44angleX : 51.30	angleY : -64.53	angleZ : 127.46
angleX : -129.10	angleY : -74.73	angleZ : -141.42angleX : 52.82	angleY : -74.16	angleZ : 105.39
angleX : -143.48	angleY : -84.34	angleZ : -134.83angleX : 60.49	angleY : -88.00	angleZ : 81.72
angleX : -146.52	angleY : -88.53	angleZ : -133.36angleX : 53.53	angleY : -114.76	angleZ : 61.34
angleX : -136.61	angleY : -104.30	angleZ : -130.40angleX : 39.21	angleY : -124.03	angleZ : 60.12
angleX : -124.26	angleY : -100.97	angleZ : -145.08angleX : 30.14	angleY : -129.92	angleZ : 73.57
angleX : -116.23	angleY : -87.55	angleZ : -171.14angleX : 37.75	angleY : -134.95	angleZ : 94.20
angleX : -109.62	angleY : -75.39	angleZ : -202.96angleX : 46.18	angleY : -92.57	angleZ : 127.20
angleX : -102.09	angleY : -71.42	angleZ : -233.15angleX : 46.48	angleY : -41.15	angleZ : 167.88
angleX : -91.65	angleY : -68.36	angleZ : -252.63angleX : 39.46	angleY : -9.71	angleZ : 196.02
angleX : -82.05	angleY : -69.39	angleZ : -256.80angleX : 37.74	angleY : -10.87	angleZ : 208.22
angleX : -82.84	angleY : -61.11	angleZ : -244.30angleX : 43.42	angleY : -27.36	angleZ : 195.11
angleX : -86.12	angleY : -53.47	angleZ : -221.68angleX : 57.33	angleY : -56.50	angleZ : 150.99
angleX : -85.02	angleY : -54.46	angleZ : -193.00angleX : 52.33	angleY : -95.53	angleZ : 124.39
angleX : -92.38	angleY : -47.73	angleZ : -164.38angleX : 54.57	angleY : -88.27	angleZ : 116.95
angleX : -96.30	angleY : -58.37	angleZ : -140.46angleX : 59.27	angleY : -97.13	angleZ : 95.84
angleX : -102.91	angleY : -74.91	angleZ : -131.15angleX : 57.73	angleY : -106.06	angleZ : 70.14
angleX : -104.11	angleY : -55.30	angleZ : -141.39angleX : 55.72	angleY : -104.43	angleZ : 69.89
angleX : -94.89	angleY : -54.64	angleZ : -158.20angleX : 44.29	angleY : -98.29	angleZ : 88.77
angleX : -87.98	angleY : -48.57	angleZ : -183.53angleX : 42.58	angleY : -96.29	angleZ : 116.81
angleX : -81.36	angleY : -42.22	angleZ : -213.11angleX : 58.23	angleY : -58.40	angleZ : 149.76
angleX : -85.10	angleY : -45.44	angleZ : -237.22angleX : 66.76	angleY : -9.65	angleZ : 190.69
angleX : -73.66	angleY : -66.13	angleZ : -249.39angleX : 59.72	angleY : 18.21	angleZ : 217.03
angleX : -76.73	angleY : -26.94	angleZ : -262.81angleX : 59.37	angleY : 35.81	angleZ : 229.79
angleX : -76.78	angleY : -21.52	angleZ : -260.67angleX : 65.59	angleY : 24.37	angleZ : 224.18
angleX : -77.78	angleY : -24.21	angleZ : -246.93angleX : 72.36	angleY : -11.13	angleZ : 184.93
angleX : -83.18	angleY : -17.52	angleZ : -216.00angleX : 64.67	angleY : -54.43	angleZ : 150.64
angleX : -88.79	angleY : -27.64	angleZ : -188.14angleX : 61.37	angleY : -79.92	angleZ : 133.12
angleX : -90.55	angleY : -34.29	angleZ : -164.39angleX : 68.34	angleY : -94.79	angleZ : 110.17
angleX : -89.24	angleY : -37.87	angleZ : -149.76angleX : 63.68	angleY : -89.63	angleZ : 89.10
angleX : -87.25	angleY : -30.93	angleZ : -155.16angleX : 67.43	angleY : -102.19	angleZ : 96.50
angleX : -80.29	angleY : -40.06	angleZ : -178.50angleX : 65.55	angleY : -96.10	angleZ : 114.83
angleX : -80.93	angleY : -48.86	angleZ : -215.51angleX : 58.95	angleY : -102.51	angleZ : 117.64
angleX : -86.74	angleY : -40.39	angleZ : -253.13angleX : 60.09	angleY : -99.28	angleZ : 139.65
angleX : -86.53	angleY : -39.96	angleZ : -272.67angleX : 71.73	angleY : -56.49	angleZ : 178.12
angleX : -82.09	angleY : -55.81	angleZ : -283.11angleX : 73.02	angleY : -9.44	angleZ : 208.19
angleX : -83.30	angleY : -32.29	angleZ : -289.69angleX : 68.26	angleY : 7.66	angleZ : 215.77
angleX : -80.72	angleY : -18.87	angleZ : -290.74angleX : 69.02	angleY : -7.09	angleZ : 203.54
angleX : -73.65	angleY : -21.02	angleZ : -276.91angleX : 71.22	angleY : -41.38	angleZ : 165.67
angleX : -74.46	angleY : -24.76	angleZ : -244.49angleX : 70.67	angleY : -80.86	angleZ : 142.12
angleX : -105.86	angleY : 12.06	angleZ : -211.82angleX : 77.78	angleY : -80.59	angleZ : 134.58
angleX : -127.82	angleY : 9.16	angleZ : -189.71angleX : 81.97	angleY : -98.52	angleZ : 121.63
angleX : -131.53	angleY : 24.59	angleZ : -163.87angleX : 79.29	angleY : -113.76	angleZ : 106.33
angleX : -127.42	angleY : 14.58	angleZ : -161.23angleX : 79.61	angleY : -98.01	angleZ : 104.62
angleX : -113.52	angleY : -1.50	angleZ : -163.41angleX : 76.79	angleY : -98.86	angleZ : 103.05
angleX : -94.84	angleY : -27.37	angleZ : -191.99angleX : 62.50	angleY : -91.74	angleZ : 113.14
angleX : -97.90	angleY : -33.18	angleZ : -241.91angleX : 56.60	angleY : -82.03	angleZ : 138.64
angleX : -106.83	angleY : -25.23	angleZ : -274.30angleX : 65.79	angleY : -57.49	angleZ : 176.33
angleX : -114.01	angleY : 13.15	angleZ : -298.02angleX : 80.28	angleY : -20.68	angleZ : 214.65
angleX : -113.06	angleY : 9.10	angleZ : -299.96angleX : 77.46	angleY : 5.00	angleZ : 226.79
angleX : -112.32	angleY : 4.09	angleZ : -295.56angleX : 77.01	angleY : 7.44	angleZ : 226.99
angleX : -112.96	angleY : 2.90	angleZ : -280.29angleX : 78.49	angleY : -16.44	angleZ : 203.77
angleX : -114.17	angleY : 0.67	angleZ : -244.93angleX : 87.57	angleY : -50.15	angleZ : 154.76
angleX : -123.76	angleY : 7.39	angleZ : -217.79angleX : 89.11	angleY : -99.30	angleZ : 129.02
angleX : -145.08	angleY : 24.70	angleZ : -194.80angleX : 96.70	angleY : -93.81	angleZ : 129.62
angleX : -156.61	angleY : -4.08	angleZ : -185.17angleX : 99.25	angleY : -95.23	angleZ : 117.05
angleX : -161.24	angleY : -11.75	angleZ : -179.72angleX : 90.89	angleY : -114.67	angleZ : 103.19
angleX : -152.04	angleY : 2.46	angleZ : -184.24angleX : 86.20	angleY : -104.54	angleZ : 98.28
angleX : -135.65	angleY : -0.65	angleZ : -190.60angleX : 83.51	angleY : -108.13	angleZ : 109.05
angleX : -114.99	angleY : -0.83	angleZ : -212.33angleX : 71.62	angleY : -120.15	angleZ : 132.78
angleX : -103.63	angleY : 3.02	angleZ : -246.20angleX : 81.71	angleY : -81.36	angleZ : 165.16
angleX : -92.90	angleY : -3.26	angleZ : -276.60angleX : 95.33	angleY : -32.01	angleZ : 198.42
angleX : -85.27	angleY : -2.44	angleZ : -295.46angleX : 91.31	angleY : 16.76	angleZ : 218.11
angleX : -80.24	angleY : 9.46	angleZ : -303.16angleX : 74.50	angleY : 2.25	angleZ : 227.04
angleX : -69.55	angleY : -6.77	angleZ : -298.24angleX : 64.06	angleY : -21.88	angleZ : 218.63
angleX : -71.73	angleY : -5.96	angleZ : -280.71angleX : 66.87	angleY : -32.51	angleZ : 176.34
angleX : -84.83	angleY : -2.17	angleZ : -241.20angleX : 76.13	angleY : -69.10	angleZ : 127.33
angleX : -110.30	angleY : 21.28	angleZ : -206.92angleX : 68.34	angleY : -86.87	angleZ : 107.22
angleX : -115.33	angleY : -10.98	angleZ : -174.97angleX : 68.42	angleY : -114.42	angleZ : 99.60
angleX : -129.39	angleY : -4.75	angleZ : -162.30angleX : 62.40	angleY : -120.76	angleZ : 89.89
angleX : -135.78	angleY : -13.65	angleZ : -164.29angleX : 58.81	angleY : -123.24	angleZ : 84.53
angleX : -125.49	angleY : -33.02	angleZ : -177.53angleX : 67.15	angleY : -123.44	angleZ : 94.54
angleX : -118.36	angleY : -17.18	angleZ : -211.28angleX : 59.96	angleY : -99.06	angleZ : 116.26
angleX : -115.72	angleY : 10.25	angleZ : -247.43angleX : 64.38	angleY : -73.59	angleZ : 145.34
angleX : -96.83	angleY : 21.35	angleZ : -283.22angleX : 74.28	angleY : -30.86	angleZ : 178.54
angleX : -83.46	angleY : 23.93	angleZ : -306.36angleX : 73.18	angleY : 14.73	angleZ : 204.79
angleX : -75.16	angleY : 27.58	angleZ : -316.33angleX : 74.22	angleY : 26.68	angleZ : 219.20
angleX : -70.34	angleY : 23.79	angleZ : -311.07angleX : 73.42	angleY : 1.98	angleZ : 217.59
angleX : -69.93	angleY : 16.41	angleZ : -285.19angleX : 80.34	angleY : -18.86	angleZ : 192.72
angleX : -66.91	angleY : 3.88	angleZ : -251.27angleX : 86.56	angleY : -32.53	angleZ : 155.65
angleX : -62.92	angleY : -11.21	angleZ : -226.96angleX : 92.36	angleY : -59.64	angleZ : 140.03
angleX : -44.69	angleY : -52.25	angleZ : -215.06angleX : 91.85	angleY : -87.82	angleZ : 117.07
angleX : -48.37	angleY : -36.92	angleZ : -200.03angleX : 86.78	angleY : -97.56	angleZ : 90.36
angleX : -52.71	angleY : -60.72	angleZ : -202.46angleX : 86.92	angleY : -101.62	angleZ : 96.78
angleX : -45.04	angleY : -59.88	angleZ : -216.06angleX : 84.41	angleY : -103.69	angleZ : 121.77
angleX : -42.75	angleY : -50.35	angleZ : -244.10angleX : 81.35	angleY : -110.52	angleZ : 144.37
angleX : -46.10	angleY : -49.25	angleZ : -274.60angleX : 94.91	angleY : -101.04	angleZ : 170.32
angleX : -51.37	angleY : -38.09	angleZ : -307.37angleX : 114.47	angleY : -51.02	angleZ : 191.38
angleX : -47.85	angleY : -46.56	angleZ : -318.98angleX : 120.82	angleY : -17.96	angleZ : 201.60
angleX : -50.66	angleY : -45.12	angleZ : -319.34angleX : 120.89	angleY : -13.15	angleZ : 204.08
angleX : -57.23	angleY : -28.88	angleZ : -307.52angleX : 119.32	angleY : -34.05	angleZ : 186.92
angleX : -66.01	angleY : -27.23	angleZ : -282.16angleX : 128.26	angleY : -66.52	angleZ : 165.11
angleX : -83.91	angleY : -24.69	angleZ : -247.40angleX : 135.69	angleY : -60.68	angleZ : 154.29
angleX : -102.78	angleY : -38.36	angleZ : -229.45angleX : 129.17	angleY : -86.78	angleZ : 137.02
angleX : -103.81	angleY : -65.07	angleZ : -212.39angleX : 116.66	angleY : -115.73	angleZ : 124.78
angleX : -99.18	angleY : -87.02	angleZ : -215.19angleX : 106.44	angleY : -112.83	angleZ : 116.07
angleX : -100.67	angleY : -91.97	angleZ : -221.16angleX : 105.18	angleY : -103.78	angleZ : 102.49
angleX : -86.99	angleY : -83.58	angleZ : -240.82angleX : 103.00	angleY : -88.48	angleZ : 112.24
angleX : -80.09	angleY : -82.37	angleZ : -277.93angleX : 103.01	angleY : -81.74	angleZ : 140.19
angleX : -75.63	angleY : -65.61	angleZ : -305.11angleX : 110.91	angleY : -41.22	angleZ : 173.56
angleX : -70.66	angleY : -58.85	angleZ : -323.43angleX : 108.01	angleY : -8.45	angleZ : 201.55
angleX : -60.05	angleY : -70.21	angleZ : -328.92angleX : 99.75	angleY : 3.52	angleZ : 210.56
angleX : -56.53	angleY : -66.85	angleZ : -327.47angleX : 99.00	angleY : 1.31	angleZ : 204.82
angleX : -59.23	angleY : -75.21	angleZ : -317.73angleX : 106.64	angleY : -17.16	angleZ : 177.99
angleX : -73.02	angleY : -72.86	angleZ : -281.15angleX : 118.50	angleY : -38.38	angleZ : 170.38
angleX : -69.90	angleY : -103.10	angleZ : -243.59angleX : 121.45	angleY : -58.46	angleZ : 167.53
angleX : -58.21	angleY : -106.69	angleZ : -219.77angleX : 113.69	angleY : -92.71	angleZ : 148.73
angleX : -58.81	angleY : -113.21	angleZ : -202.84angleX : 104.49	angleY : -117.61	angleZ : 132.72
angleX : -67.50	angleY : -107.07	angleZ : -193.97angleX : 97.59	angleY : -108.35	angleZ : 133.55
angleX : -64.15	angleY : -65.85	angleZ : -199.66angleX : 96.40	angleY : -101.84	angleZ : 145.13
angleX : -54.87	angleY : -15.73	angleZ : -183.77angleX : 91.40	angleY : -85.88	angleZ : 163.96
angleX : -19.58	angleY : -38.40	angleZ : -196.05angleX : 101.36	angleY : -53.41	angleZ : 196.44
angleX : 4.50	angleY : -45.36	angleZ : -228.02angleX : 112.22	angleY : -6.17	angleZ : 225.46
angleX : 8.34	angleY : -58.99	angleZ : -246.10angleX : 115.93	angleY : 25.97	angleZ : 241.90
angleX : 14.46	angleY : -50.00	angleZ : -253.09angleX : 111.86	angleY : 16.55	angleZ : 241.99
angleX : 12.55	angleY : -45.86	angleZ : -257.97angleX : 111.15	angleY : -7.05	angleZ : 225.36
angleX : 14.17	angleY : -65.86	angleZ : -249.14angleX : 114.38	angleY : -16.39	angleZ : 191.45
angleX : 14.86	angleY : -71.16	angleZ : -211.88angleX : 128.29	angleY : -46.76	angleZ : 174.91
angleX : 2.88	angleY : -36.09	angleZ : -168.88angleX : 137.57	angleY : -62.48	angleZ : 159.95
angleX : -25.48	angleY : -19.38	angleZ : -163.53angleX : 137.78	angleY : -93.74	angleZ : 142.95
angleX : -23.61	angleY : -47.99	angleZ : -137.72angleX : 131.15	angleY : -109.38	angleZ : 133.05
angleX : -16.07	angleY : -51.93	angleZ : -128.28angleX : 122.83	angleY : -107.39	angleZ : 133.57
angleX : -18.15	angleY : -46.88	angleZ : -143.20angleX : 119.52	angleY : -98.09	angleZ : 145.81
angleX : -18.53	angleY : -35.82	angleZ : -172.91angleX : 108.83	angleY : -70.87	angleZ : 173.34
angleX : -15.35	angleY : -38.57	angleZ : -215.74angleX : 106.24	angleY : -50.00	angleZ : 216.09
angleX : -9.36	angleY : -22.30	angleZ : -255.15angleX : 109.81	angleY : -20.44	angleZ : 251.92
angleX : -5.48	angleY : -15.19	angleZ : -270.33angleX : 113.76	angleY : 20.02	angleZ : 271.88
angleX : -7.45	angleY : -16.01	angleZ : -271.91angleX : 123.47	angleY : 23.10	angleZ : 278.48
angleX : -11.59	angleY : -19.25	angleZ : -257.03angleX : 131.25	angleY : -6.31	angleZ : 259.73
angleX : -23.40	angleY : -22.32	angleZ : -221.09angleX : 136.25	angleY : -44.10	angleZ : 217.77
angleX : -40.30	angleY : -25.11	angleZ : -193.39angleX : 137.66	angleY : -86.85	angleZ : 208.32
angleX : -58.15	angleY : -16.40	angleZ : -167.85angleX : 141.26	angleY : -102.47	angleZ : 191.38
angleX : -63.70	angleY : -9.95	angleZ : -151.52angleX : 135.51	angleY : -149.88	angleZ : 179.09
angleX : -66.50	angleY : -11.83	angleZ : -151.12angleX : 123.66	angleY : -151.59	angleZ : 165.71
angleX : -56.11	angleY : -1.58	angleZ : -158.15angleX : 121.82	angleY : -152.74	angleZ : 171.09
angleX : -37.59	angleY : 29.22	angleZ : -163.42angleX : 114.07	angleY : -148.22	angleZ : 183.64
angleX : -20.17	angleY : -20.68	angleZ : -173.74angleX : 109.04	angleY : -136.41	angleZ : 198.81
angleX : 2.31	angleY : -39.47	angleZ : -199.37angleX : 116.22	angleY : -100.82	angleZ : 235.96
angleX : 30.27	angleY : -59.55	angleZ : -225.89angleX : 120.63	angleY : -49.86	angleZ : 272.33
angleX : 36.43	angleY : -55.62	angleZ : -233.88angleX : 120.16	angleY : -10.03	angleZ : 286.11
angleX : 36.25	angleY : -54.98	angleZ : -226.61angleX : 121.26	angleY : -14.24	angleZ : 287.79
angleX : 23.18	angleY : -53.71	angleZ : -202.69angleX : 127.13	angleY : -51.11	angleZ : 266.33
angleX : -3.03	angleY : -41.60	angleZ : -156.56angleX : 130.27	angleY : -80.75	angleZ : 227.27
angleX : -17.22	angleY : -50.53	angleZ : -156.47angleX : 135.27	angleY : -90.24	angleZ : 211.04
angleX : -18.59	angleY : -80.05	angleZ : -143.37angleX : 144.91	angleY : -106.28	angleZ : 193.17
angleX : -25.57	angleY : -71.32	angleZ : -131.29angleX : 142.75	angleY : -130.93	angleZ : 167.50
angleX : -31.21	angleY : -56.29	angleZ : -135.09angleX : 135.90	angleY : -126.21	angleZ : 170.62
angleX : -32.40	angleY : -49.11	angleZ : -147.35angleX : 130.34	angleY : -131.79	angleZ : 192.01
angleX : -19.43	angleY : -55.93	angleZ : -157.42angleX : 128.26	angleY : -137.58	angleZ : 199.14
angleX : -2.33	angleY : -50.73	angleZ : -184.48angleX : 122.68	angleY : -131.94	angleZ : 193.86
angleX : -3.19	angleY : -46.14	angleZ : -220.21angleX : 124.96	angleY : -79.85	angleZ : 227.66
angleX : -3.07	angleY : -33.13	angleZ : -243.87angleX : 118.92	angleY : -29.87	angleZ : 255.64
angleX : -0.84	angleY : -7.81	angleZ : -259.61angleX : 109.92	angleY : -5.83	angleZ : 267.61
angleX : -2.39	angleY : -4.25	angleZ : -257.43angleX : 103.04	angleY : -30.62	angleZ : 272.52
angleX : -16.43	angleY : -15.55	angleZ : -235.04angleX : 106.95	angleY : -73.23	angleZ : 257.13
angleX : -38.46	angleY : -4.58	angleZ : -197.21angleX : 112.30	angleY : -77.07	angleZ : 234.74
angleX : -55.95	angleY : -11.58	angleZ : -189.90angleX : 120.17	angleY : -101.14	angleZ : 217.25
angleX : -71.65	angleY : -34.81	angleZ : -173.66angleX : 119.52	angleY : -130.99	angleZ : 189.57
angleX : -76.23	angleY : -49.74	angleZ : -161.17angleX : 110.66	angleY : -124.78	angleZ : 141.99
angleX : -84.22	angleY : -44.02	angleZ : -164.57angleX : 92.94	angleY : -131.68	angleZ : 158.44
angleX : -82.71	angleY : -32.48	angleZ : -172.19angleX : 90.05	angleY : -134.32	angleZ : 177.27
angleX : -75.00	angleY : -27.36	angleZ : -174.13angleX : 83.47	angleY : -143.17	angleZ : 198.47
'''
mylist=re.findall('angleZ : -*[0-9]{1,}\.[0-9]{2}a',mystr);
templist1=[]
templist2=[]
for i in range(len(mylist)):
    templist1.append(mylist[i][9:])
    templist2.append(float(templist1[i][:-1]))
plt.plot(range(len(templist2)),templist2,'y-',label='Hand')

mylist=re.findall('angleZ : -*[0-9]{1,}\.[0-9]{2}\n',mystr);
templist3=[]
templist4=[]
for i in range(len(mylist)):
    templist3.append(mylist[i][9:])
    templist4.append(float(templist3[i][:-1]))
plt.plot(range(len(templist4)),templist4,'b-',label='Foot')
plt.grid()
plt.xlabel('Times')
plt.ylabel('Angles')
plt.title('2 Angles by Axis Z')
plt.legend()
ax=plt.gca()
x_major_locator=MultipleLocator(20)
y_major_locator=MultipleLocator(40)
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
plt.savefig('/Users/yangan/Desktop/result__.png', dpi=300) #指定分辨率保存
