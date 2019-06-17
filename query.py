import v4l2capture
path="/dev/video0"
video = v4l2capture.Video_device(path)

print(video.get_info())
print(video.get_exposure_auto())

video.close()
