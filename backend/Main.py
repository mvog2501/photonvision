import tornado.ioloop

from app.ChameleonVisionApp import ChameleonApplication
from app.classes.SettingsManager import SettingsManager
from tornado.options import options
from app.handlers.CamerasHandler import CamerasHandler
from app.handlers.VisionHandler import VisionHandler

if __name__ == "__main__":
    # SettingsManager()
    CamerasHandler.init_camera()

    VisionHandler().run()

    tornado.options.parse_command_line()
    app = ChameleonApplication()
    print(f"Serving on port {options.port}")
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

#TODO: create process for each camera
# create proccess loop and camera publisher
# bridge network tables for each camera