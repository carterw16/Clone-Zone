Windows Portable Demo
If you just want to use OpenPose without compiling or writing any code, simply use the latest portable version of OpenPose for Windows.

For maximum speed, you should use OpenPose in a machine with a Nvidia GPU version. If so, you must upgrade your Nvidia drivers to the latest version (in the Nvidia "GeForce Experience" software or its website).
Download the latest OpenPose version from the Releases section.
https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases

Notes: I used v1.7.0



Follow the Instructions.txt file inside the downloaded zip file to download the models required by OpenPose.(Doesn't work, please download model here: https://www.kaggle.com/datasets/changethetuneman/openpose-model)

Then, you can run OpenPose from the PowerShell command-line by running: bin\OpenPoseDemo.exe --video examples/media/video.avi --write_json [your output folder]
Note: If you are using the GPU-accelerated version and are seeing Cuda check failed (3 vs. 0): initialization error when running OpenPose, you can fix it by doing one of these:

Upgrade your Nvidia drivers. If the error persists, make sure your machine does not contain any CUDA version (or if so, that it's the same than the OpenPose portable demo files). Otherwise, uninstall that CUDA version. If you need to keep that CUDA version installed, follow Compiling and Running OpenPose from Source for that particular CUDA version instead.
Download an older OpenPose version (v1.6.0 does not show this error).
