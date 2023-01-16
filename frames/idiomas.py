class Idiomas:
    
    def __init__(self, idioma="es_ES"):
        """_summary_

            Por defecto, el idioma es Espanol

        Args:
            idioma (str, optional): _description_. Defaults to "es_ES".

        Raises:
            Exception: _description_
        """
        
        self.es_ES = "es_ES" # Español
        self.en_US = "en_US" # Ingles
        self.zh_CN = "zh_CN" # Chino
        self.ru_RU = "ru_RU" # Ruso 
        self.fr_FR = "fr_FR" # Frances(Francia)
        self.ar_EG = "ar_EG" # Arabe Egipto(el mas similar al estandar)
        self.ja_JP = "ja_JP" # Japones
        self.de_DE = "de_DE" # Aleman(Alemania)
        self.esperanto = "esperanto" # esperanto
        
        self.ALL_LENGUAJE = [
            self.es_ES, 
            self.en_US, 
            self.zh_CN,
            self.ru_RU,
            self.fr_FR,
            self.ar_EG,
            self.ja_JP,
            self.de_DE,
            self.esperanto
        ]
        
        self.idioma = idioma
        print(self.idioma)
        
        if self.es_ES == self.idioma: # Español
            # textos de errores:
            self.TextPortError = "El puerto introducido no se encuentra en el rango 1 - 2**16."
            self.TextHostError = "Este no es un host valido, introduzca 'localhost' o una direcion IPv4 valida."
            self.TextDirErrorNotFoundOrNotExists = "Este directorio no existe o no se pudo encontrar."
            self.TextThisNotDir = "Lo introducido no es un directorio, es un archivo posiblemente."
            self.TextUrlNotFound = "Usted no introducio ningun enlace o este no es valido :("
            self.TextUnknownError = "Ocurrio un error desconocido."
            self.TextErrorDeConexion = "No se pudo conectar a internet."
            self.TextUnknownOS = "No se pudo identificar el OS en el que se esta trabajando."
            self.TextNotFoundThisFile = "Este idioma no tiene un archivo de ayuda disponible."
            self.TextNotExistsThisLenguaje = "Este idioma no esta registrado en la lista."
            self.TextNotExistsResolution = "Esta resolucion no esta en disponible para este enlace: " 
            # textos del memu:
            self.ForMoreInformation = "Para mas informacion"
            self.InformationOfAutor = "Informacion del autor"
            self.Help = "Ayuda"
            self.AboutThisSoftware = "Sobre este software"
            self.ExtraTools = "Herramientas-Extras"
            self.DownloadAVideo = "Descargar un unico video"
            self.DownloadVideoToPlaylits = "Descargar una playlist de videos"
            self.DownloadMusic = "Descargar un unico archivo .mp3"
            self.DownloadMusicToPlaylist = "Descargar una playlist de musica"
            self.idiomasText = "Idiomas"
            self.exit = "Salir"
            self.ajustes = "Ajustes"
            # textos frame1.py
            self.info = "\nPrograma creado en Python para \ndescargar videos de Youtube\n"
            self.url_video = "Url del video -> "
            self.dir_file = "Carpeta donde ingresar el archivo -> "
            self.download_text = "Descargar"
            self.calidad_video_text = "Calidad de video -> " 
            # textos frame2.py
            self.info2 = "\nApartado para descargar \nuna playlist de video\n" 
            self.url_playlist = "Url de la playlist -> " 
            self.dir_file_playlist = "Carpeta donde almacenar\nel contenido de la play list ->" 
            # textos frame3.py
            self.info3 = "\nApartado para descargar\nuna cancion en formato mp3\n" 
            # textos frame4.py 
            self.info4 = "\nApartado para descargar una\nplaylist de musica en formato mp3\n" 
            # textos setting.py
            self.fecha_creacion = "Proyecto creado el {} por {}".format("10-10-10", "Maalfer")
            self.disponible = "Disponible en :\n{}\n{}".format("https://github.com/desmonHak/Youtube_Downloader", "https://github.com/Maalfer/Youtube_Downloader")
            self.aboutThis = "Este proyecto permite \ndescargar contenido de YouTube."
            
        elif self.en_US == self.idioma: # Ingles
            self.TextPortError = "The entered port is not in the range 1 - 2**16"
            self.TextHostError = "This is not a valid host, enter 'localhost' or a valid IPv4 address"
            self.TextDirErrorNotFoundOrNotExists = "This directory does not exist or could not be found"
            self.TextThisNotDir = "What is entered is not a directory, it is a file possibly."
            self.TextUrlNotFound = "You did not enter any link or it is not valid :("
            self.TextUnknownError = "An unknown error occurred"
            self.TextErrorDeConexion = "Could not connect to the internet"
            self.TextUnknownOS = "Could not identify the OS being worked on"
            self.TextNotFoundThisFile = "This language does not have a help file available."
            self.TextNotExistsThisLenguaje = "This language is not registered in the list."
            self.TextNotExistsResolution = "This resolution is not available for this link: " 
            # textos del memu:
            self.ForMoreInformation = "For more information"
            self.InformationOfAutor = "Author information"
            self.Help = "Help"
            self.AboutThisSoftware = "About this software"
            self.ExtraTools = "Extra-Tools"
            self.DownloadAVideo = "Download a single video"
            self.DownloadVideoToPlaylits = "Download a playlist of videos"
            self.DownloadMusic = "Download a single .mp3 file"
            self.DownloadMusicToPlaylist = "Download a music playlist"
            self.idiomasText = "Languages"
            self.exit = "Exit"
            self.ajustes = "Ajustes"
            # textos frame1.py
            self.info = "\nProgram created in Python to \ndownload videos from Youtube\n"
            self.url_video = "video url -> "
            self.dir_file = "Folder where to put the file -> "
            self.download_text = "Download"
            self.calidad_video_text = "video quality-> " 
            # textos frame2.py
            self.info2 = "\nSection to download \na video playlist\n" 
            self.url_playlist = "playlist url -> " 
            self.dir_file_playlist = "Folder to store\nthe content of the playlist ->" 
            # textos frame3.py
            self.info3 = "\nSection to download\na song in mp3 format\n" 
            # textos frame4.py 
            self.info4 = "\nSection to download a\nmp3 music playlist\n" 
            # textos setting.py
            self.fecha_creacion = "Proyecto creado el {} por {}".format("10-10-10", "Maalfer")
            self.disponible = "Disponible en :\n{}\n{}".format("https://github.com/desmonHak/Youtube_Downloader", "https://github.com/Maalfer/Youtube_Downloader")
            self.aboutThis = "Este proyecto permite \ndescargar contenido de YouTube."
            
        elif self.zh_CN == self.idioma: # Chino
            self.TextPortError = "输入的端口不在 1 - 2**16 范围内"
            self.TextHostError = "这不是有效的主机，请输入“localhost”或有效的 IPv4 地址"
            self.TextDirErrorNotFoundOrNotExists = "该目录不存在或找不到"
            self.TextThisNotDir = "输入的不是目录，可能是文件。"
            self.TextUrlNotFound = " 您没有输入任何链接或者您输入都是链接无效 :("
            self.TextUnknownError = "出现未知错误"
            self.TextErrorDeConexion = "无法连接到互联网"
            self.TextUnknownOS = "无法识别正在使用的操作系统"
            self.TextNotFoundThisFile = "该语言没有可用的帮助文件。"
            self.TextNotExistsThisLenguaje = "该语言未在列表中注册。"
            self.TextNotExistsResolution = "此分辨率不适用于此链接: " 
            # textos del memu:
            self.ForMoreInformation = "想要查询更多的信息"
            self.InformationOfAutor = "作者信息"
            self.Help = "帮助"
            self.AboutThisSoftware = "关于本软件"
            self.ExtraTools = "工具-附加"
            self.DownloadAVideo = "下载单个视频"
            self.DownloadVideoToPlaylits = "下载视频播放列表"
            self.DownloadMusic = "下载单个 .mp3 文件"
            self.DownloadMusicToPlaylist = "下载音乐播放列表"
            self.idiomasText = "语言"
            self.exit = "出去"
            self.ajustes = "Ajustes"
            # textos frame1.py
            self.info = "\n在 Python 中创建的程序 \n下载 Youtube 视频\n"
            self.url_video = "视频网址 -> "
            self.dir_file = "放置文件的文件夹 -> "
            self.download_text = "释放"
            self.calidad_video_text = "视频质量 -> " 
            # textos frame2.py
            self.info2 = "\n下载部分 \n视频播放列表\n" 
            self.url_playlist = "播放列表网址 -> " #
            self.dir_file_playlist = "要存储的文件夹\n播放列表的内容 ->" 
            # textos frame3.py
            self.info3 = "\n下载部分\n一首mp3格式的歌曲\n" 
            # textos frame4.py 
            self.info4 = "\n下载部分\nmp3 音乐播放列表\n" 
            # textos setting.py
            self.fecha_creacion = "Proyecto creado el {} por {}".format("10-10-10", "Maalfer")
            self.disponible = "Disponible en :\n{}\n{}".format("https://github.com/desmonHak/Youtube_Downloader", "https://github.com/Maalfer/Youtube_Downloader")
            self.aboutThis = "Este proyecto permite \ndescargar contenido de YouTube."
            
        elif self.ru_RU == self.idioma: # Ruso 
            self.TextPortError = "Введенный порт не находится в диапазоне 1–2**16"
            self.TextHostError = "Это недопустимый хост, введите «localhost» или действительный адрес IPv4."
            self.TextDirErrorNotFoundOrNotExists = "Этот каталог не существует или не может быть найден"
            self.TextThisNotDir = "То, что вводится, не является каталогом, возможно, это файл."
            self.TextUrlNotFound = "Вы не ввели ссылку или она недействительна :("
            self.TextUnknownError = "Произошла неизвестная ошибка"
            self.TextErrorDeConexion = "Не удалось подключиться к Интернету"
            self.TextUnknownOS = "Не удалось определить ОС, над которой ведется работа"
            self.TextNotFoundThisFile = "Для этого языка нет файла справки."
            self.TextNotExistsThisLenguaje = "Этот язык не зарегистрирован в списке."
            self.TextNotExistsResolution = "Это разрешение недоступно для этой ссылки: " 
            # textos del memu:
            self.ForMoreInformation = "Для дополнительной информации"
            self.InformationOfAutor = "Информация об авторе"
            self.Help = "Помощь"
            self.AboutThisSoftware = "Об этом программном обеспечении"
            self.ExtraTools = "Инструменты-дополнения"
            self.DownloadAVideo = "Скачать одно видео"
            self.DownloadVideoToPlaylits = "Скачать плейлист видео"
            self.DownloadMusic = "Скачать один файл .mp3"
            self.DownloadMusicToPlaylist = "Скачать музыкальный плейлист"
            self.idiomasText = "Языки"
            self.ajustes = "Ajustes"
            self.exit = "Выйти"
            # textos frame1.py
            self.info = "\nПрограмма, созданная на Python для \nскачать видео с ютуба\n"
            self.url_video = "URL-адрес видео -> "
            self.dir_file = "Папка куда положить файл -> "
            self.download_text = "Увольнять"
            self.calidad_video_text = "качество видео -> " 
            # textos frame2.py
            self.info2 = "\nРаздел для скачивания\nвидео плейлист\n" 
            self.url_playlist = "URL плейлиста -> " 
            self.dir_file_playlist = "Папка для хранения\nсодержание плейлиста ->" 
            # textos frame3.py
            self.info3 = "\nРаздел для скачивания\nпесня в формате mp3\n" 
            # textos frame4.py 
            self.info4 = "\nРаздел для скачивания\nмузыкальный плейлист в формате mp3\n" 
            # textos setting.py
            self.fecha_creacion = "Proyecto creado el {} por {}".format("10-10-10", "Maalfer")
            self.disponible = "Disponible en :\n{}\n{}".format("https://github.com/desmonHak/Youtube_Downloader", "https://github.com/Maalfer/Youtube_Downloader")
            self.aboutThis = "Este proyecto permite \ndescargar contenido de YouTube."
            
        elif self.fr_FR == self.idioma: # Frances(Francia)
            self.TextPortError = "Le port saisi n'est pas dans la plage 1 - 2**16"
            self.TextHostError = "Ce n'est pas un hôte valide, entrez 'localhost' ou une adresse IPv4 valide"
            self.TextDirErrorNotFoundOrNotExists = "Ce répertoire n'existe pas ou est introuvable"
            self.TextThisNotDir = "Ce qui est entré n'est pas un répertoire, c'est éventuellement un fichier."
            self.TextUrlNotFound = "Vous n'avez entré aucun lien ou il est invalide :("
            self.TextUnknownError = "Une erreur inconnue est survenue"
            self.TextErrorDeConexion = "Impossible de se connecter à Internet"
            self.TextUnknownOS = "Impossible d'identifier le système d'exploitation sur lequel on travaille"
            self.TextNotFoundThisFile = "Cette langue n'a pas de fichier d'aide disponible."
            self.TextNotExistsThisLenguaje = "Cette langue n'est pas enregistrée dans la liste."
            self.TextNotExistsResolution = "Cette résolution n'est pas disponible pour ce lien: " 
            # textos del memu:
            self.ForMoreInformation = "Pour plus d'informations"
            self.InformationOfAutor = "Informations sur l'auteur"
            self.Help = "Aider"
            self.AboutThisSoftware = "À propos de ce logiciel"
            self.ExtraTools = "Outils supplémentaires"
            self.DownloadAVideo = "Télécharger une seule vidéo"
            self.DownloadVideoToPlaylits = "Télécharger une playlist de vidéos"
            self.DownloadMusic = "Télécharger un seul fichier .mp3"
            self.DownloadMusicToPlaylist = "Télécharger une playlist musicale"
            self.idiomasText = "langues"
            self.exit = "sortir"
            self.ajustes = "Ajustes"
            # textos frame1.py
            self.info = "\nProgramme créé en Python pour \ntélécharger des vidéos Youtube\n"
            self.url_video = "URL de la vidéo -> "
            self.dir_file = "Dossier où mettre le fichier -> "
            self.download_text = "Décharge"
            self.calidad_video_text = "qualité vidéo -> " 
            # textos frame2.py
            self.info2 = "\nRubrique à télécharger \nune liste de lecture vidéo\n" 
            self.url_playlist = "URL de la liste de lecture -> " 
            self.dir_file_playlist = "Dossier à stocker\nle contenu de la playlist ->" 
            # textos frame3.py
            self.info3 = "\nRubrique à télécharger\nune chanson au format mp3\n" 
            # textos frame4.py 
            self.info4 = "\nRubrique pour télécharger un\nliste de lecture de musique mp3\n" 
            # textos setting.py
            self.fecha_creacion = "Proyecto creado el {} por {}".format("10-10-10", "Maalfer")
            self.disponible = "Disponible en :\n{}\n{}".format("https://github.com/desmonHak/Youtube_Downloader", "https://github.com/Maalfer/Youtube_Downloader")
            self.aboutThis = "Este proyecto permite \ndescargar contenido de YouTube."
            
        elif self.ar_EG == self.idioma: # Arabe Egipto(el mas similar al estandar)
            self.TextPortError = "المنفذ الذي تم إدخاله ليس في النطاق 1 - 2 ** 16"
            self.TextHostError = """هذا ليس مضيفًا صالحًا ، أدخل "localhost" أو عنوان IPv4 صالحًا"""
            self.TextDirErrorNotFoundOrNotExists = "هذا الدليل غير موجود أو تعذر العثور عليه"
            self.TextThisNotDir = "ما تم إدخاله ليس دليلاً ، ربما يكون ملفًا."
            self.TextUrlNotFound = "لم تقم بإدخال أي ارتباط أو أنه غير صالح :( "
            self.TextUnknownError = "حدث خطأ غير معروف"
            self.TextErrorDeConexion = "تعذر الاتصال بالإنترنت"
            self.TextUnknownOS = "تعذر تحديد نظام التشغيل قيد العمل"
            self.TextNotFoundThisFile = "لا يتوفر ملف تعليمات لهذه اللغة."
            self.TextNotExistsThisLenguaje = "هذه اللغة غير مسجلة في القائمة."
            self.TextNotExistsResolution = "هذا القرار غير متاح لهذا الارتباط: " 
            # textos del memu:
            self.ForMoreInformation = "للمزيد من المعلومات"
            self.InformationOfAutor = "معلومات الكاتب"
            self.Help = "يساعد"
            self.AboutThisSoftware = "حول هذا البرنامج"
            self.ExtraTools = "أدوات - إضافات"
            self.DownloadAVideo = "تنزيل مقطع فيديو واحد"
            self.DownloadVideoToPlaylits = "قم بتنزيل قائمة تشغيل مقاطع الفيديو"
            self.DownloadMusic = "تنزيل ملف mp3 واحد"
            self.DownloadMusicToPlaylist = "قم بتنزيل قائمة تشغيل الموسيقى"
            self.idiomasText = "اللغات"
            self.exit = "أخرج"
            self.ajustes = "Ajustes"
            # textos frame1.py
            self.info = "\n برنامج تم إنشاؤه في Python من أجل \n تنزيل مقاطع فيديو YouTube \n"
            self.url_video = "رابط الفيديو -> "
            self.dir_file = "المجلد حيث يتم وضع الملف -> "
            self.download_text = "تسريح"
            self.calidad_video_text = "جودة الفيديو -> " 
            # textos frame2.py
            self.info2 = "\nقسم للتحميل \nقائمة تشغيل الفيديو\n" 
            self.url_playlist = "عنوان url لقائمة التشغيل -> " 
            self.dir_file_playlist = "مجلد للتخزين\nمحتوى قائمة التشغيل ->" 
            # textos frame3.py
            self.info3 = "\nقسم للتحميل\nأغنية بتنسيق mp3\n" 
            # textos frame4.py 
            self.info4 = "\nقسم للتحميل أ\nقائمة تشغيل موسيقى mp3\n" 
            # textos setting.py
            self.fecha_creacion = "Proyecto creado el {} por {}".format("10-10-10", "Maalfer")
            self.disponible = "Disponible en :\n{}\n{}".format("https://github.com/desmonHak/Youtube_Downloader", "https://github.com/Maalfer/Youtube_Downloader")
            self.aboutThis = "Este proyecto permite \ndescargar contenido de YouTube."
            
        elif self.ja_JP == self.idioma: # Japones
            self.TextPortError = "入力されたポートは 1 から 2**16 の範囲にありません"
            self.TextHostError = "これは有効なホストではありません。「localhost」または有効な IPv4 アドレスを入力してください"
            self.TextDirErrorNotFoundOrNotExists = "このディレクトリは存在しないか、見つかりませんでした"
            self.TextThisNotDir = "入力されるのはディレクトリではなく、おそらくファイルです。"
            self.TextUrlNotFound = "リンクを入力していないか、有効ではありません:("
            self.TextUnknownError = "不明なエラーが発生しました"
            self.TextErrorDeConexion = "インターネットに接続できませんでした"
            self.TextUnknownOS = "動作しているOSを特定できませんでした"
            self.TextNotFoundThisFile = "この言語には、利用できるヘルプ ファイルがありません。"
            self.TextNotExistsThisLenguaje = "この言語はリストに登録されていません。"
            self.TextNotExistsResolution = "この解像度は、このリンクでは利用できません: "
            # textos del memu:
            self.ForMoreInformation = "詳細については"
            self.InformationOfAutor = "著者情報"
            self.Help = "ヘルプ"
            self.AboutThisSoftware = "このソフトウェアについて"
            self.ExtraTools = "ツール - エクストラ"
            self.DownloadAVideo = "単一のビデオをダウンロードする"
            self.DownloadVideoToPlaylits = "動画のプレイリストをダウンロードする"
            self.DownloadMusic = "単一の .mp3 ファイルをダウンロードする"
            self.DownloadMusicToPlaylist = "音楽プレイリストをダウンロードする"
            self.idiomasText = "言語"
            self.exit = "外出"
            self.ajustes = "Ajustes"
            # textos frame1.py
            self.info = "\nPython で作成されたプログラム \nユーチューブの動画をダウンロード\n"
            self.url_video = "動画の URL -> "
            self.dir_file = "ファイルを置くフォルダ -> "
            self.download_text = "放電"
            self.calidad_video_text = "ビデオ品質 -> " 
            # textos frame2.py
            self.info2 = "\nダウンロードするセクション \nビデオのプレイリスト\n" 
            self.url_playlist = "再生リストの URL -> " #
            self.dir_file_playlist = "格納するフォルダ\nプレイリストの内容 ->" 
            # textos frame3.py
            self.info3 = "\nダウンロードするセクション\nmp3形式の曲\n" 
            # textos frame4.py 
            self.info4 = "\nダウンロードするセクション\nmp3 音楽プレイリスト\n" 
            # textos setting.py
            self.fecha_creacion = "Proyecto creado el {} por {}".format("10-10-10", "Maalfer")
            self.disponible = "Disponible en :\n{}\n{}".format("https://github.com/desmonHak/Youtube_Downloader", "https://github.com/Maalfer/Youtube_Downloader")
            self.aboutThis = "Este proyecto permite \ndescargar contenido de YouTube."
            
        elif self.de_DE == self.idioma: # Aleman(Alemania)
            self.TextPortError = "Der eingegebene Port liegt nicht im Bereich 1 - 2**16"
            self.TextHostError = "Dies ist kein gültiger Host, geben Sie „localhost“ oder eine gültige IPv4-Adresse ein"
            self.TextDirErrorNotFoundOrNotExists = "Dieses Verzeichnis existiert nicht oder konnte nicht gefunden werden"
            self.TextThisNotDir = "Was eingetragen wird, ist kein Verzeichnis, sondern möglicherweise eine Datei."
            self.TextUrlNotFound = "Sie haben keinen Link eingegeben oder er ist ungültig :("
            self.TextUnknownError = "Ein unbekannter Fehler ist aufgetreten"
            self.TextErrorDeConexion = "Es konnte keine Verbindung zum Internet hergestellt werden"
            self.TextUnknownOS = "Das Betriebssystem, an dem gearbeitet wird, konnte nicht identifiziert werden"
            self.TextNotFoundThisFile = "Für diese Sprache ist keine Hilfedatei verfügbar."
            self.TextNotExistsThisLenguaje = "Diese Sprache ist nicht in der Liste registriert."
            self.TextNotExistsResolution = "Diese Auflösung ist für diesen Link nicht verfügbar: " 
            # textos del memu:
            self.ForMoreInformation = "Für mehr Informationen"
            self.InformationOfAutor = "Informationen zum Autor"
            self.Help = "Hilfe"
            self.AboutThisSoftware = "Über diese Software"
            self.ExtraTools = "Zusätzliche Werkzeuge"
            self.DownloadAVideo = "Laden Sie ein einzelnes Video herunter"
            self.DownloadVideoToPlaylits = "Laden Sie eine Playlist mit Videos herunter"
            self.DownloadMusic = "Laden Sie eine einzelne .mp3-Datei herunter"
            self.DownloadMusicToPlaylist = "Laden Sie eine Musikwiedergabeliste herunter"
            self.idiomasText = "Sprachen"
            self.exit = "Hinausgehen"
            self.ajustes = "Ajustes"
            # textos frame1.py
            self.info = "\nIn Python erstelltes Programm zu \nYouTube-Videos herunterladen\n"
            self.url_video = "Video-URL -> "
            self.dir_file = "Ordner, in dem die Datei abgelegt werden soll -> "
            self.download_text = "Entladung"
            self.calidad_video_text = "Videoqualität -> " 
            # textos frame2.py
            self.info2 = "\nRubrik zum Download \neine Video-Playlist\n" 
            self.url_playlist = "Wiedergabelisten-URL -> " 
            self.dir_file_playlist = "Ordner zu speichern\nden Inhalt der Playlist->" 
            # textos frame3.py
            self.info3 = "\nRubrik zum Download\nein Lied im mp3-Format\n" 
            # textos frame4.py 
            self.info4 = "\nAbschnitt zum Herunterladen a\nMP3-Musik-Playlist\n" 
            # textos setting.py
            self.fecha_creacion = "Proyecto creado el {} por {}".format("10-10-10", "Maalfer")
            self.disponible = "Disponible en :\n{}\n{}".format("https://github.com/desmonHak/Youtube_Downloader", "https://github.com/Maalfer/Youtube_Downloader")
            self.aboutThis = "Este proyecto permite \ndescargar contenido de YouTube."
                        
        elif self.esperanto == self.idioma: # esperanto
            self.TextPortError = "La enigita haveno ne estas en la intervalo 1 - 2**16"
            self.TextHostError = "Ĉi tio ne estas valida gastiganto, enigu 'localhost' aŭ validan IPv4-adreson"
            self.TextDirErrorNotFoundOrNotExists = "Ĉi tiu dosierujo ne ekzistas aŭ ne troveblas"
            self.TextThisNotDir = "Kio estas enigita ne estas dosierujo, ĝi estas dosiero eble."
            self.TextUrlNotFound = "Vi enigis neniun ligilon aŭ ĝi ne validas :("
            self.TextUnknownError = "Nekonata eraro okazis"
            self.TextErrorDeConexion = "Ne eblis konekti al la interreto"
            self.TextUnknownOS = "Ne eblis identigi la OS prilaborata"
            self.TextNotFoundThisFile = "Ĉi tiu lingvo ne havas disponeblan helpdosieron."
            self.TextNotExistsThisLenguaje = "Ĉi tiu lingvo ne estas registrita en la listo."
            self.TextNotExistsResolution = "Ĉi tiu rezolucio ne disponeblas por ĉi tiu ligo: " 
            # textos del memu:
            self.ForMoreInformation = "Por pliaj informoj"
            self.InformationOfAutor = "Aŭtoraj Informoj"
            self.Help = "Helpu"
            self.AboutThisSoftware = "Pri ĉi tiu programaro"
            self.ExtraTools = "Kromaj Iloj"
            self.DownloadAVideo = "Elŝutu ununuran videon"
            self.DownloadVideoToPlaylits = "Elŝutu ludliston de videoj"
            self.DownloadMusic = "Elŝutu ununuran .mp3-dosieron"
            self.DownloadMusicToPlaylist = "Elŝutu muzikliston"
            self.idiomasText = "Lingvoj"
            self.exit = "Eliru"
            self.ajustes = "Ajustes"
            # textos frame1.py
            self.info = "\nProgramo kreita en Python al \nelŝutu videojn de Youtube\n"
            self.url_video = "video URL -> "
            self.dir_file = "Dosierujo kie meti la dosieron -> "
            self.download_text = "Malŝarĝo"
            self.calidad_video_text = "videokvalito-> " 
            # textos frame2.py
            self.info2 = "\nSekcio por elŝuti \nvideolisto\n" 
            self.url_playlist = "url de la ludlisto -> " 
            self.dir_file_playlist = "Dosierujo por stoki\nla enhavo de la ludlisto ->" 
            # textos frame3.py
            self.info3 = "\nSekcio por elŝuti\nkanto en mp3-formato\n" 
            # textos frame4.py 
            self.info4 = "\nSekcio por elŝuti a\nmp3-muzika ludlisto\n" 
            # textos setting.py
            self.fecha_creacion = "Proyecto creado el {} por {}".format("10-10-10", "Maalfer")
            self.disponible = "Disponible en :\n{}\n{}".format("https://github.com/desmonHak/Youtube_Downloader", "https://github.com/Maalfer/Youtube_Downloader")
            self.aboutThis = "Este proyecto permite \ndescargar contenido de YouTube."
            
        else:
            raise Exception("Este idioma no se encuentra {}".format(self.idioma))
            
    def setIdioma(self, idioma):
        """_summary_
            Esta funcion cambia de idioma el programa
        Args:r
            idioma (str): se recibe el idioma a cambiar
        """
        print("Cambiando de idioma a:"+idioma)
        self.__init__(idioma)