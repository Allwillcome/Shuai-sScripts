import pandas as pd
import numpy as np

def saveresults():
    listofVariablesNames = listofvariables()
    return pd.DataFrame(columns = listofVariablesNames)
     
def updatedataframe(dfresults, pat, testT, sensors, asymmetryResults):
    listofVariablesNames = listofvariables()
    leftFoot = sensors['leftfoot'] 
    rightFoot = sensors['rightfoot'] 
    lowBack= sensors['lowback']
    
    listofVariables = [
            pat,
            testT,
            leftFoot.stridetimemean,
            leftFoot.stridetimeSTD,
            leftFoot.normstridetime,
            leftFoot.meanStrideDistperstep,
            leftFoot.stdStrideDistperstep,
            leftFoot.kmph,
            leftFoot.cadence,
            leftFoot.meanstrideVelperstepperstep,
            leftFoot.stdstrideVelperstepperstep,
            leftFoot.accrangeAP,

            leftFoot.accrmsAP,
            leftFoot.accrangeML,

            leftFoot.accrmsML,
            leftFoot.accrangeVT,
            leftFoot.accrmsVT,
            leftFoot.gyrrangeAP,
            leftFoot.gyrrmsAP,
            leftFoot.gyrrangeML,
            leftFoot.gyrrmsML,
            leftFoot.gyrrangeVT,
            leftFoot.gyrrmsVT,
            leftFoot.fftsignalML.dominantpeak,
            leftFoot.fftsignalML.width,
            leftFoot.fftsignalML.slope,
            leftFoot.fftsignalML.SDP,
            leftFoot.autocovx_acc,
            leftFoot.autocovy_acc,
            leftFoot.autocovz_acc,
            leftFoot.autocovx_gyr,
            leftFoot.autocovy_gyr,
            leftFoot.autocovz_gyr,
            leftFoot.autocorx_acc,
            leftFoot.autocory_acc,
            leftFoot.autocorz_acc,
            leftFoot.autocorx_gyr,
            leftFoot.autocory_gyr,
            leftFoot.autocorz_gyr,
            leftFoot.lde[0],
            leftFoot.lde[1],
            leftFoot.lde[2],
            leftFoot.approxentropy_accX ,                              
            leftFoot.approxentropy_accY ,
            leftFoot.approxentropy_accZ ,
            leftFoot.sampleEntropy_accX ,                
            leftFoot.sampleEntropy_accY ,
            leftFoot.sampleEntropy_accZ,
            rightFoot.stridetimemean,
            rightFoot.stridetimeSTD,
            rightFoot.normstridetime,
            rightFoot.meanStrideDistperstep,
            rightFoot.stdStrideDistperstep,
            rightFoot.kmph,
            rightFoot.cadence,
            rightFoot.meanstrideVelperstepperstep,
            rightFoot.stdstrideVelperstepperstep,
            rightFoot.accrangeAP,
            rightFoot.accrmsAP,
            rightFoot.accrangeML,
            rightFoot.accrmsML,
            rightFoot.accrangeVT,
            rightFoot.accrmsVT,
            rightFoot.gyrrangeAP,
            rightFoot.gyrrmsAP,
            rightFoot.gyrrangeML,
            rightFoot.gyrrmsML,
            rightFoot.gyrrangeVT,
            rightFoot.gyrrmsVT,
            rightFoot.fftsignalML.dominantpeak,
            rightFoot.fftsignalML.width,
            rightFoot.fftsignalML.slope,
            rightFoot.fftsignalML.SDP,
            rightFoot.autocovx_acc,
            rightFoot.autocovy_acc,
            rightFoot.autocovz_acc,
            rightFoot.autocovx_gyr,
            rightFoot.autocovy_gyr,
            rightFoot.autocovz_gyr,
            rightFoot.autocorx_acc,
            rightFoot.autocory_acc,
            rightFoot.autocorz_acc,
            rightFoot.autocorx_gyr,
            rightFoot.autocory_gyr,
            rightFoot.autocorz_gyr,
            rightFoot.lde[0],
            rightFoot.lde[1],
            rightFoot.lde[2],
            rightFoot.approxentropy_accX ,                              
            rightFoot.approxentropy_accY ,
            rightFoot.approxentropy_accZ ,
            rightFoot.sampleEntropy_accX ,                
            rightFoot.sampleEntropy_accY ,
            rightFoot.sampleEntropy_accZ,
            lowBack.stridetimemean,
            lowBack.stridetimeSTD,
            lowBack.normstridetime,
            lowBack.accrangeAP,
            lowBack.accrmsAP,
            lowBack.accrangeML,
            lowBack.accrmsML,
            lowBack.accrangeVT,
            lowBack.accrmsVT,
            lowBack.gyrrangeAP,
            lowBack.gyrrmsAP,
            lowBack.gyrrangeML,
            lowBack.gyrrmsML,
            lowBack.gyrrangeVT,
            lowBack.gyrrmsVT,
            lowBack.fftsignalAP.dominantpeak,
            lowBack.fftsignalAP.width,
            lowBack.fftsignalAP.slope,
            lowBack.fftsignalAP.SDP,
            lowBack.fftsignalAP.harmonicratio,
            lowBack.fftsignalAP.harmonicindex,
            lowBack.fftsignalML.dominantpeak,
            lowBack.fftsignalML.width,
            lowBack.fftsignalML.slope,
            lowBack.fftsignalML.SDP,
            lowBack.fftsignalML.harmonicratio,
            lowBack.fftsignalML.harmonicindex,
            lowBack.fftsignalVT.dominantpeak,
            lowBack.fftsignalVT.width,
            lowBack.fftsignalVT.slope,
            lowBack.fftsignalVT.SDP,
            lowBack.fftsignalVT.harmonicratio,
            lowBack.fftsignalVT.harmonicindex,
            lowBack.autocovx_acc,
            lowBack.autocovy_acc,
            lowBack.autocovz_acc,
            lowBack.autocovx_gyr,
            lowBack.autocovy_gyr,
            lowBack.autocovz_gyr,
            lowBack.autocorx_acc,
            lowBack.autocory_acc,
            lowBack.autocorz_acc,
            lowBack.autocorx_gyr,
            lowBack.autocory_gyr,
            lowBack.autocorz_gyr,
            lowBack.lde[0],
            lowBack.lde[1],
            lowBack.lde[2],
            lowBack.approxentropy_accX ,                              
            lowBack.approxentropy_accY ,
            lowBack.approxentropy_accZ ,
            lowBack.sampleEntropy_accX ,                
            lowBack.sampleEntropy_accY ,
            lowBack.sampleEntropy_accZ,
            asymmetryResults.SRswing_stance,
            asymmetryResults.SRstandphase,
            asymmetryResults.SRswingphase,
            asymmetryResults.SIswing_stancePar,   
            asymmetryResults.SIstandphase,             
            asymmetryResults.SIswingphase,       
            asymmetryResults.GAswing_stancePar,   
            asymmetryResults.GAstandphase,            
            asymmetryResults.GAswingphase,
            asymmetryResults.SAswing_stancePar,       
            asymmetryResults.SAstandphase,           
            asymmetryResults.SAswingphase,    
            asymmetryResults.stepPeakDiffSTD,
            asymmetryResults.lowBackPeakDiffValues,
            asymmetryResults.Amplitudeasym,
            asymmetryResults.AmplitudeSTDasym,
            asymmetryResults.normDistance,
            asymmetryResults.normCadence,
            asymmetryResults.normDistancePStride,
            asymmetryResults.normTimePerStep
]#
    tmpdf = pd.DataFrame(data = np.array([listofVariables]), 
                         columns = listofVariablesNames)
    
    dfresults = pd.concat([dfresults, tmpdf], axis = 0, ignore_index = True) #阿帅批：修改 append 为 concat
    # dfresults = dfresults.append(tmpdf, ignore_index = True) 
    return dfresults

def listofvariables():
    return [
        'Subject number',
        'Test Type',
        # Left foot
        'Stride time mean L',
        'Stride time std L',
        'Stride time norm L',
        'Stride dist mean L',
        'Stride dist std L',
        'KMPH L',
        'Cadence L',
        'Stride vel mean L',
        'Stride vel std L', 

        'Range acc AP L', 
        'RMS acc AP L', 
        'Range acc ML L', 
        'RMS acc ML L', 
        'Range acc VT L', 
        'RMS acc VT L', 
        'Range gyr AP L', 
        'RMS gyr AP L', 
        'Range gyr ML L', 
        'RMS gyr ML L', 
        'Range gyr VT L', 
        'RMS gyr VT L', 

        'Dominant peak freq L',
        'Dominant peak width L',
        'Dominant peak slope L',
        'Dominant peak density L',

        'ACOV acc AP L',
        'ACOV acc ML L',
        'ACOV acc VT L',
        'ACOV gyr AP L',
        'ACOV gyr ML L',
        'ACOV gyr VT L',
        'ACOR acc AP L',
        'ACOR acc ML L',
        'ACOR acc VT L',
        'ACOR gyr AP L',
        'ACOR gyr ML L',
        'ACOR gyr VT L',

        'LDE AP L',
        'LDE ML L',
        'LDE VT L',

        'ApEn AP L',                              
        'ApEn ML L',    
        'ApEn VT L',    
        'SampEN AP L',                
        'SampEN ML L',      
        'SampEN VT L',      
        # Right foot
        'Stride time mean R',
        'Stride time std R',
        'Stride time norm R',
        'Stride dist mean R',
        'Stride dist std R',
        'KMPH R',
        'Cadence R',
        'Stride vel mean R',
        'Stride vel std R', 

        'Range acc AP R', 
        'RMS acc AP R', 
        'Range acc MR R', 
        'RMS acc MR R', 
        'Range acc VT R', 
        'RMS acc VT R', 
        'Range gyr AP R', 
        'RMS gyr AP R', 
        'Range gyr MR R', 
        'RMS gyr MR R', 
        'Range gyr VT R', 
        'RMS gyr VT R', 

        'Dominant peak freq R',
        'Dominant peak width R',
        'Dominant peak slope R',
        'Dominant peak density R',

        'ACOV acc AP R',
        'ACOV acc MR R',
        'ACOV acc VT R',
        'ACOV gyr AP R',
        'ACOV gyr MR R',
        'ACOV gyr VT R',
        'ACOR acc AP R',
        'ACOR acc MR R',
        'ACOR acc VT R',
        'ACOR gyr AP R',
        'ACOR gyr MR R',
        'ACOR gyr VT R',

        'LDE AP R',
        'LDE MR R',
        'LDE VT R',

        'ApEn AP R',                              
        'ApEn MR R',    
        'ApEn VT R',    
        'SampEN AP R',                
        'SampEN MR R',      
        'SampEN VT R',  

        # Low back
        'Step time mean B',
        'Step time std B',
        'Step time norm B',

        'Range acc AP B', 
        'Rms acc AP B', 
        'Range acc ML B', 
        'Rms acc ML B', 
        'Range acc VT B', 
        'Rms acc VT B', 
        'Range gyr AP B', 
        'Rms gyr AP B', 
        'Range gyr ML B', 
        'Rms gyr ML B', 
        'Range gyr VT B', 
        'Rms gyr VT B', 

        'Dominant peak freq AP B',
        'Dominant peak width AP B',
        'Dominant peak slope AP B',
        'Dominant peak density AP B',
        'HR AP B',
        'IH AP B',

        'Dominant peak freq ML B',
        'Dominant peak width ML B',
        'Dominant peak slope ML B',
        'Dominant peak density ML B',
        'HR ML B',
        'IH ML B',

        'Dominant peak freq VT B',
        'Dominant peak width VT B',
        'Dominant peak slope VT B',
        'Dominant peak density VT B',
        'HR VT B',
        'IH VT B',

        'ACOV acc AP B',
        'ACOV acc ML B',
        'ACOV acc VT B',
        'ACOV gyr AP B',
        'ACOV gyr ML B',
        'ACOV gyr VT B',
        'ACOR acc AP B',
        'ACOR acc ML B',
        'ACOR acc VT B',
        'ACOR gyr AP B',
        'ACOR gyr ML B',
        'ACOR gyr VT B',

        'LDE AP B',
        'LDE ML B',
        'LDE VT B',

        'ApEn AP B',                              
        'ApEn ML B',    
        'ApEn VT B',    
        'SampEN AP B',                
        'SampEN ML B',      
        'SampEN VT B',  

        'SR Swing/stand',
        'SR standphasess',
        'SR swingphases',
        'SI Swing/stand',   
        'SI standphases',             
        'SI swingphases',       
        'GA Swing/stand',   
        'GA standphases',            
        'GA swingphases',
        'SA Swing/stand',       
        'SA standphases',           
        'SA swingphases',    
        'Peak amp mean B: L/R',
        'Peak amp std B: L/R',
        'Peak amp mean L/R',
        'Peak amp std L/R',
        'Total Dist norm',
        'Cadence norm',
        'Stride dist mean norm',
        'Stride time mean norm',
        ]


