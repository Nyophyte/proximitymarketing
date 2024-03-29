# -*- coding: utf-8 -*-
BASE_SIGNAL=20000
END_SIGNAL=BASE_SIGNAL+1000

NO_DONGLES		=BASE_SIGNAL+0
DONGLES_ADDED		=BASE_SIGNAL+1
CYCLE_OPTY_DONGLE	=BASE_SIGNAL+2

TOO_BUSY		=BASE_SIGNAL+10

CONNECTED		=BASE_SIGNAL+100
DISCONNECTED		=BASE_SIGNAL+101
CONNECTION_FAILED	=BASE_SIGNAL+102

HANDLE_OK		=BASE_SIGNAL+200
HANDLE_LOST_CONNECTION	=BASE_SIGNAL+201
HANDLE_PICTURE		=BASE_SIGNAL+202

TEXT={
    NO_DONGLES: 'NO_DONGLES',
    DONGLES_ADDED: 'DONGLES_ADDED',
    CYCLE_OPTY_DONGLE: 'CYCLE_OPTY_DONGLE',
    TOO_BUSY: 'TOO_BUSY',
    CONNECTED: 'CONNECTED',
    DISCONNECTED: 'DISCONNECTED',
    CONNECTION_FAILED: 'CONNECTION_FAILED',
    HANDLE_OK: 'HANDLED_OK',
    HANDLE_LOST_CONNECTION: 'HANDLED_LOST_CONNECTION',
    HANDLE_PICTURE: 'HANDLED_PICTURE',
}

def isCameraSignal(val):
    return val >= BASE_SIGNAL and val <= END_SIGNAL
