# bascorro_cv

## To do in nearby future

- **Using custom compiled opencv-contrib library with OPENMP enabled**

open mp will enable pararell processing, which will allow us to utilize all four core in our raspi
but as mentioned [here](https://stackoverflow.com/questions/37337828/openmp-how-to-use-all-available-cpu-to-improve-performance),
the improvement not really significant, but still worth to try

  really usefull links
  - https://stackoverflow.com/questions/29494503/how-to-compile-opencv-with-openmp
  - http://answers.opencv.org/question/103701/how-opencv-use-openmp-thread-to-get-performance/
    
- **Research about the encoding that being used in the realtime video processing**

**if** you still using usb web cam, while based on the previous experience, seems not very bad, the problem with the usb webcam is that the encoding process of the realtime video will hogging the cpu so much by theory (but somehow seems not really happening), rather than if you're using raspi camera which will utilize the GPU to do the encoding, so probably this also worth to research
  

- **MUST Buy Raspi CAM**

as i mention earlier, this also worth to try
 + lot of people mention about using good driver for raspi cam, 
 
 >The Pi camera is 'run' by the GPU and can dump full frames into RAM at 15 frames a second .. this is 7.5MB/frame, 15fps = 112.5 Mega >BYTES per second .. or you can have full HD resolution 30fps H264 encoded (by the GPU) along with some simultaneous still photos (Google >MMAL) all at virtually zero CPU loading ..

>On the other hand, the Pi USB is 'run' byte at a time by the CPU, and, at the cost of 100% CPU loading you might achieve a couple of >hundred Mega BITS per second .. not that a web cam is going to deliver that anyway (even if it could, you then don't have any CPU cycles >to do anything with it ..)

>SO, unless CCTV resolutions (320x240 pixels) are what you want, it has to be the Pi camera.

  Reference links
  - https://www.raspberrypi.org/forums/viewtopic.php?t=221425
  - https://www.raspberrypi.org/forums/viewtopic.php?t=207554
  - https://www.raspberrypi.org/forums/viewtopic.php?t=116828
  - https://raspberrypi.stackexchange.com/questions/48032/advantages-of-raspberry-pi-15-pin-mipi-camera-interface-csi-connector-cameras
  
- **Update raspi to last version**

  uselfull links 
    - [Raspbian strecth](https://www.raspberrypi.org/blog/raspbian-stretch/)
    

- **Update your code to fit with OpenCV 4**

opencv 4 as mentioned in its website offers more feature, and some new algorithm, not really mentioning about performance increase, but we're expecting there is no performance degradation, so this also worth to try

  Usefull links 
   - https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/

- **Reseach about designing the code that fits into CPU Cache**

Good code will utilize the cpu cache and expected to be less likely to dumping the preprocessed data into ram (or even secondary memory)
so this also worth to try

  Reference links
  - https://stackoverflow.com/questions/763262/how-does-one-write-code-that-best-utilizes-the-cpu-cache-to-improve-performance
  - https://stackoverflow.com/questions/1822295/design-code-to-fit-in-cpu-cache
  
  
- **Multithreading the code**
 
 (perhaps) i already implemented this by the time you reading this, but still worth to research if any better library than imutils WebcamVideoStream
 
   Usefull links
    - https://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/
    - https://www.pyimagesearch.com/2015/12/28/increasing-raspberry-pi-fps-with-python-and-opencv/
    
    ps : imho pyimageresearch still the best for providing topic about opencv, makesure you check it 
    
  
