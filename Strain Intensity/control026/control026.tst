BEGIN_FILE
	Version 1.0
	Collection CellScaleBiaxial

BEGIN_BLOCK

BEGIN_DEVICES
1	csGen2	COM3	AutoDetectCOM	UniAxial	LoadcellX	5000	28.5821	Temperature	37	ThreadsPerInch 6	AllowCompressionTestModes	NoExternalSync
	PreloadEx 2 250 50 600 5 8 100

BEGIN_CAMERAS
1	LogitechWebCam	Focus 30

BEGIN_DISPLAYS
1	Video	1	Live_Video	777	583	443	333	FixedAspectRatio

BEGIN_CHARTS
1	Force_N	FAuto	0	2	Time_S	Scroll	0	10	Position	600	0
	Series	1	X	(255,0,0)	2
2	Displacement_mm	FAuto	0	30	Time_S	Scroll	0	10	Position	600	350
	Series	1	X	(255,0,0)	2
3	Force_N	FAuto	0	2	Displacement_mm	FAuto	0	30	Position	600	700	ClearBetweenCycles
	Series	1	X	(255,0,0)	2

BEGIN_HARDWAREOPTS
TemplateHardwareVersion	2
TemperatureSetPoint	37
PreloadSettingsEx2 2 250 50 600 5 8 7 100
IdleCurrent 1
SyncPulseDivisor -1
TestMode TENSION
CameraType	WebCam
CameraShutter	15
CameraGain	10
CameraFocus	30


BEGIN_CONTROLS
Timestamp	Seconds
SampleSizeX_um	70000
SampleSizeY_um	4700
NumTrueStrainSegments	10
NumDataAveragingPoints	1
SizeAdjustWithPreload
SoftLimits	500	150000	100	40000
SoftForceLimits2	-1	25000
TemperatureWarnings	0	1
ResetWarning	1
ZeroWarning	0
SystemCompensation	0
OutputColumns	SetName	Cycle	Time_S	Size_mm	Displacement_mm	Force_N

BEGIN_MULTISET
Name	XMode	XFunction	XUnits	XMagnitude	XPreloadType	XPreloadMag	YMode	YFunction	YUnits	YMagnitude	YPreloadType	YPreloadMag	StretchDurationSec	RecoveryDurationSec	HoldTimeSec	RestTimeSec	NumReps	DataFreqHz	ImageFreqHz	SendCOM	
lightguide100stretch	Disp	Ramp	%	0.5	None	100	Disp	Ramp	um	0	None	100	0.1	0	0.1	0	100	5	1	0	_	
