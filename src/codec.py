#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_comp_data_dx50():
    """ Encoder: MPEG4, FourCC: DX50 """

    return '2935,"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"'
 
 
def get_comp_data_h264_43():
    """ Encoder: H.264; FourCC: H.264, Bitrate 1200 kbs, Darstellungsverhältnis 4:3 
        von monarc99 aus Thread, einzige Änderung: reframes auf 4 """   
    
    return '2951,"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"'

def get_comp_data_h264_169():
    """ Encoder: H.264; FourCC: H.264, Bitrate 1200 kbs, Darstellungsverhältnis 16:9
        von monarc99 aus Thread, einzige Änderung: reframes auf 4 """   
    
    return '2952,"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"'
