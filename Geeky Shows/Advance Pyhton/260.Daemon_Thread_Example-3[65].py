from threading import current_thread
mt=current_thread()
print(mt.getName())
print(mt.daemon)