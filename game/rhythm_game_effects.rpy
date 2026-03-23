################################################################################
## RHYTHM MINIGAME - ABBA Dance Scene
################################################################################
init python:

    ABBA_NOTE_CHART = [
        (0.639, 3),
        (1.521, 3),
        (2.403, 3),
        (2.844, 1),
        (3.286, 3),
        (3.715, 0),
        (4.168, 2),
        (4.609, 0),
        (4.818, 0),
        (5.039, 2),
        (5.480, 0),
        (5.921, 2),
        (6.142, 0),
        (6.815, 2),
        (7.465, 0),
        (7.697, 2),
        (8.348, 0),
        (8.568, 2),
        (9.009, 0),
        (9.451, 3),
        (10.333, 2),
        (11.006, 3),
        (11.227, 2),
        (11.447, 1),
        (12.109, 3),
        (12.992, 2),
        (13.874, 3),
        (14.756, 3),
        (15.639, 3),
        (16.521, 3),
        (16.962, 0),
        (17.403, 3),
        (17.845, 0),
        (18.286, 3),
        (19.168, 3),
        (20.050, 2),
        (20.480, 0),
        (20.921, 3),
        (21.142, 0),
        (21.815, 2),
        (22.477, 2),
        (22.698, 3),
        (22.918, 3),
        (23.568, 2),
        (24.009, 1),
        (24.451, 3),
        (24.903, 0),
        (25.345, 3),
        (25.786, 2),
        (26.006, 3),
        (26.227, 2),
        (27.098, 1),
        (27.759, 0),
        (27.980, 1),
        (28.630, 0),
        (28.851, 2),
        (29.292, 0),
        (29.733, 2),
        (30.383, 0),
        (30.604, 2),
        (31.045, 0),
        (31.475, 2),
        (32.357, 3),
        (33.019, 1),
        (33.239, 3),
        (34.110, 1),
        (34.551, 1),
        (34.981, 2),
        (35.863, 2),
        (36.513, 0),
        (36.734, 3),
        (37.396, 0),
        (37.616, 2),
        (38.487, 2),
        (38.708, 1),
        (39.369, 3),
        (40.240, 2),
        (40.461, 1),
        (40.902, 1),
        (41.123, 2),
        (42.005, 1),
        (42.887, 2),
        (43.654, 1),
        (43.770, 2),
        (44.652, 3),
        (45.302, 1),
        (45.534, 2),
        (45.964, 1),
        (46.417, 3),
        (46.626, 1),
        (46.846, 1),
        (47.067, 1),
        (47.299, 3),
        (47.740, 0),
        (47.949, 1),
        (48.181, 3),
        (49.064, 3),
        (49.284, 1),
        (49.505, 1),
        (49.958, 1),
        (50.178, 1),
        (50.399, 0),
        (50.608, 1),
        (50.736, 1),
        (50.840, 3),
        (51.734, 3),
        (51.955, 1),
        (52.396, 1),
        (52.616, 1),
        (52.837, 0),
        (53.058, 0),
        (53.510, 2),
        (53.731, 1),
        (53.952, 0),
        (54.172, 3),
        (54.393, 3),
        (54.613, 1),
        (55.066, 0),
        (55.275, 3),
        (55.531, 0),
        (55.716, 1),
        (55.937, 0),
        (56.169, 3),
        (56.831, 0),
        (57.051, 3),
        (57.504, 1),
        (57.725, 0),
        (57.945, 3),
        (58.607, 0),
        (58.839, 3),
        (59.083, 0),
        (59.281, 0),
        (59.501, 0),
        (59.722, 3),
        (59.966, 0),
        (60.383, 0),
        (60.604, 3),
        (60.848, 0),
        (61.057, 3),
        (61.289, 3),
        (61.510, 3),
        (62.171, 0),
        (62.380, 2),
        (62.833, 0),
        (63.286, 1),
        (63.507, 0),
        (64.168, 2),
        (64.830, 0),
        (65.062, 2),
        (65.724, 0),
        (65.945, 2),
        (66.397, 0),
        (66.839, 3),
        (67.059, 0),
        (67.500, 1),
        (67.733, 1),
        (67.953, 2),
        (68.394, 2),
        (68.615, 2),
        (68.836, 1),
        (69.509, 2),
        (70.391, 2),
        (70.832, 0),
        (71.274, 3),
        (71.494, 0),
        (72.156, 3),
        (73.038, 2),
        (73.480, 0),
        (73.921, 2),
        (74.141, 0),
        (74.803, 3),
        (75.233, 0),
        (75.685, 2),
        (76.568, 3),
        (77.450, 2),
        (77.880, 0),
        (78.321, 2),
        (78.541, 0),
        (79.215, 2),
        (79.877, 2),
        (80.097, 3),
        (80.318, 2),
        (80.747, 0),
        (80.968, 3),
        (81.409, 0),
        (81.850, 3),
        (82.083, 0),
        (82.512, 1),
        (82.744, 1),
        (82.965, 2),
        (83.406, 3),
        (83.627, 3),
        (83.847, 1),
        (84.509, 1),
        (85.391, 2),
        (86.274, 2),
        (86.494, 0),
        (87.156, 2),
        (88.038, 1),
        (88.921, 3),
        (89.792, 1),
        (90.686, 2),
        (91.347, 0),
        (91.568, 2),
        (92.439, 1),
        (93.333, 3),
        (93.542, 0),
        (94.215, 3),
        (94.656, 3),
        (94.877, 3),
        (95.097, 3),
        (95.318, 3),
        (95.747, 0),
        (95.968, 2),
        (96.409, 0),
        (96.850, 3),
        (97.083, 2),
        (97.303, 3),
        (97.733, 3),
        (97.953, 1),
        (98.174, 0),
        (98.395, 1),
        (98.615, 2),
        (99.486, 1),
        (100.148, 0),
        (100.368, 3),
        (101.018, 0),
        (101.239, 2),
        (101.680, 0),
        (102.121, 2),
        (102.772, 0),
        (102.992, 2),
        (103.863, 2),
        (104.525, 1),
        (104.745, 3),
        (105.628, 3),
        (106.069, 0),
        (106.498, 1),
        (106.940, 1),
        (107.369, 3),
        (108.251, 2),
        (108.681, 0),
        (108.902, 0),
        (109.122, 2),
        (110.005, 3),
        (110.434, 0),
        (110.875, 2),
        (111.758, 3),
        (112.187, 2),
        (112.408, 2),
        (112.628, 3),
        (112.849, 3),
        (113.070, 0),
        (113.290, 1),
        (113.511, 2),
        (113.731, 1),
        (114.393, 2),
        (115.287, 2),
        (116.181, 3),
        (117.087, 1),
        (117.307, 1),
        (117.528, 0),
        (117.748, 1),
        (117.981, 2),
        (118.201, 1),
        (118.642, 0),
        (118.875, 3),
        (119.095, 1),
        (119.316, 1),
        (119.536, 1),
        (119.769, 3),
        (120.221, 0),
        (120.442, 1),
        (120.662, 3),
        (120.883, 1),
        (121.556, 2),
        (121.777, 0),
        (122.450, 2),
        (122.683, 1),
        (122.903, 1),
        (123.240, 1),
        (123.344, 3),
        (124.250, 2),
        (124.471, 0),
        (124.912, 1),
        (125.144, 2),
        (125.806, 1),
        (126.038, 2),
        (126.259, 0),
        (126.479, 0),
        (126.711, 3),
        (126.932, 1),
        (127.152, 3),
        (127.385, 0),
        (127.826, 3),
        (128.267, 1),
        (128.708, 3),
        (129.161, 0),
        (129.602, 1),
        (130.485, 2),
        (131.146, 0),
        (131.367, 2),
        (132.249, 3),
        (133.132, 1),
        (133.573, 0),
        (134.014, 1),
        (134.235, 1),
        (134.896, 3),
        (135.117, 1),
        (135.779, 2),
        (136.661, 1),
        (137.102, 1),
        (137.543, 2),
        (138.426, 2),
        (138.867, 0),
        (139.308, 2),
        (139.970, 0),
        (140.190, 1),
        (140.632, 0),
        (141.073, 1),
        (141.293, 1),
        (141.955, 3),
        (142.838, 3),
        (143.279, 0),
        (143.720, 2),
        (144.161, 0),
        (144.602, 2),
        (145.485, 1),
        (145.926, 1),
        (146.367, 2),
        (147.029, 0),
        (147.249, 3),
        (148.132, 2),
        (148.793, 2),
        (149.235, 3),
        (149.676, 2),
        (150.117, 3),
        (150.779, 1),
        (151.220, 1),
        (151.661, 2),
        (152.543, 1),
        (153.426, 2),
        (154.308, 2),
        (155.191, 1),
        (156.073, 3),
        (156.955, 3),
        (157.838, 2),
        (158.279, 0),
        (158.720, 1),
        (159.602, 1),
        (160.485, 1),
        (161.367, 1),
        (162.249, 0),
        (163.352, 1),
        (165.558, 0),
    ]

    ## -------------------------------------------------------------------
    ## RHYTHM GAME STATE
    ## -------------------------------------------------------------------

    class RhythmGameState(object):

        NOTE_SPEED       = 400.0   ## Pixels per second notes fall
        HIT_ZONE_Y       = 900     ## Y position of the hit zone (px from top)
        SPAWN_Y          = -60     ## Y position notes spawn at
        HIT_WINDOW       = 0.15    ## Seconds either side counts as a hit
        LANE_KEYS        = ["a", "s", "k", "l"]
        LANE_COLOURS     = ["#e63946", "#f4a261", "#2a9d8f", "#457b9d"]
        LANE_LABELS      = ["A", "S", "K", "L"]

        def __init__(self, chart):
            import time
            self.chart        = sorted(chart, key=lambda n: n[0])
            self.notes        = []   
            self.next_index   = 0    
            self.score        = 0
            self.total        = len(chart)
            self.hits         = 0
            self.feedback     = [""] * 4
            self.feedback_t   = [0.0] * 4
            self.start_time   = None
            self.elapsed      = 0.0
            self.running      = True
            self.finished     = False

        def start(self):
            import time
            self.start_time = time.time()

        def update(self):
            import time
            if self.start_time is None or not self.running:
                return
            self.elapsed = time.time() - self.start_time

            ## Spawn notes whose time has come
            travel_time = (self.HIT_ZONE_Y - self.SPAWN_Y) / self.NOTE_SPEED
            while (self.next_index < len(self.chart) and
                self.chart[self.next_index][0] <= self.elapsed + travel_time):
                t, lane = self.chart[self.next_index]
                self.notes.append({
                    "id":    self.next_index,
                    "lane":  lane,
                    "time":  t,
                    "hit":   False,
                    "miss":  False,
                })
                self.next_index += 1

            ## Move notes and mark misses
            for note in self.notes:
                if note["hit"] or note["miss"]:
                    continue
                age = self.elapsed - note["time"]
                note["y"] = self.HIT_ZONE_Y + age * self.NOTE_SPEED
                if age > self.HIT_WINDOW:
                    note["miss"] = True

            ## Clean up notes that have fallen off screen
            self.notes = [n for n in self.notes
                        if not n["miss"] or n["y"] < 1200]

            ## Check finished
            if (self.next_index >= len(self.chart) and
                    all(n["hit"] or n["miss"] for n in self.notes)):
                self.finished = True
                self.running  = False

        def press_lane(self, lane):
            ## Find the closest unhit note in this lane within the hit window
            best     = None
            best_gap = self.HIT_WINDOW
            for note in self.notes:
                if note["lane"] != lane or note["hit"] or note["miss"]:
                    continue
                gap = abs(self.elapsed - note["time"])
                if gap <= best_gap:
                    best_gap = gap
                    best     = note
            if best is not None:
                best["hit"] = True
                self.hits  += 1
                self.score += max(100, int(100 * (1.0 - best_gap / self.HIT_WINDOW)))
                self.feedback[lane]   = "HIT!"
                self.feedback_t[lane] = self.elapsed
            else:
                self.feedback[lane]   = "MISS"
                self.feedback_t[lane] = self.elapsed

        def note_y(self, note):
            age = self.elapsed - note["time"]
            return self.HIT_ZONE_Y + age * self.NOTE_SPEED

        @property
        def percent(self):
            if self.total == 0:
                return 0
            return int(100 * self.hits / self.total)

        @property
        def perfect(self):
            return self.hits == self.total

    ## Global state instance, created fresh each run
    _rhythm_state = None

    def run_rhythm_game():
        """
        Called from script.rpy.
        Pauses Ren'Py, shows the rhythm screen, and returns the result.
        """
        global _rhythm_state
        _rhythm_state = RhythmGameState(ABBA_NOTE_CHART)
        renpy.call_screen("rhythm_game_screen")
        return {
            "score":   _rhythm_state.score,
            "total":   _rhythm_state.total,
            "hits":    _rhythm_state.hits,
            "perfect": _rhythm_state.perfect,
            "percent": _rhythm_state.percent,
        }


# ---------------------------------------------------------
# COUNTDOWN FUNCTION + SCREEN 
# ---------------------------------------------------------
init python:

    def rhythm_countdown():
        for t in ["3", "2", "1", "GO!"]:
            store.countdown_text = t
            renpy.show_screen("rhythm_countdown")
            renpy.pause(0.8)
        renpy.hide_screen("rhythm_countdown")

screen rhythm_countdown():
    zorder 300

    add Solid("#00000055")

    text "[countdown_text]":
        xalign 0.5
        yalign 0.5
        size 120
        color "#ffcc00"


################################################################################
## RHYTHM GAME SCREEN
################################################################################
screen rhythm_intro_screen():

    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        background "#000000cc"

        vbox:
            spacing 30
            xalign 0.5

            text "RHYTHM MINI-GAME" size 60 color "#ffcc00" xalign 0.5

            text "Hit the notes in time with the music!" size 40 xalign 0.5
            text "Use keys:  A   S   K   L" size 40 xalign 0.5
            text "Press the matching key when the note reaches the hit zone." size 32 xalign 0.5
            text "Try to get as many hits as possible!" size 32 xalign 0.5

            null height 20

            textbutton "Start!" action Return(True):
                xalign 0.5
                padding (20, 10)
                background "#ffcc00"
                text_color "#000"
                text_size 40

screen rhythm_game_start():
    timer 0.01 action Return()

screen rhythm_game_screen():
    on "show" action Play("music", audio.abba)
    modal True
    zorder 150

    ## --- Lane backgrounds ---
    hbox:
        xfill True
        yfill True
        spacing 4

        for lane_i in range(4):
            frame:
                xfill True
                yfill True

    ## --- Lane dividers and hit zone bar ---
    add Solid("#333333"):
        xpos 0
        ypos config.screen_height - 180
        xsize config.screen_width
        ysize 4

    ## --- Hit zone targets ---
    hbox:
        xfill True
        ypos config.screen_height - 180
        spacing 4
        for lane_i in range(4):
            frame:
                xfill True
                ysize 80
                background _rhythm_state.LANE_COLOURS[lane_i] + "55"
                has vbox
                xfill True
                text _rhythm_state.LANE_LABELS[lane_i]:
                    xalign 0.5 yalign 0.5
                    size 40
                    color _rhythm_state.LANE_COLOURS[lane_i]

    ## --- Falling notes (drawn each frame via a timer-driven refresh) ---
    python:
        if _rhythm_state.start_time is None:
            _rhythm_state.start()
        _rhythm_state.update()

    for note in _rhythm_state.notes:
        if not note["hit"]:
            $ note_y_pos = _rhythm_state.note_y(note)
            $ lane_w = config.screen_width // 4
            $ note_x = note["lane"] * lane_w + lane_w // 2 - 40
            frame:
                xpos note_x
                ypos int(note_y_pos) - 30
                xsize 80
                ysize 60
                background _rhythm_state.LANE_COLOURS[note["lane"]]
                has vbox
                null height 10
                text "♪":
                    xalign 0.5
                    size 30
                    color "#ffffff"

    ## --- Feedback text per lane ---
    for lane_i in range(4):
        if _rhythm_state.feedback[lane_i] != "" and (_rhythm_state.elapsed - _rhythm_state.feedback_t[lane_i]) < 0.4:
            $ lane_w = config.screen_width // 4
            $ fb_x = lane_i * lane_w + lane_w // 2 - 60
            $ fb_color = "#ffffff" if _rhythm_state.feedback[lane_i] == "HIT!" else "#ff4444"
            text _rhythm_state.feedback[lane_i]:
                xpos fb_x
                ypos config.screen_height - 280
                size 50
                color fb_color
                bold True

    ## --- Score display ---
    frame:
        xalign 0.5
        ypos 20
        background "#00000099"
        padding (30, 10)
        hbox:
            spacing 60
            text "Score: [_rhythm_state.score]":
                color "#ffffff" size 36
            text "Hits: [_rhythm_state.hits]/[_rhythm_state.total]":
                color "#ffffff" size 36
            text "[_rhythm_state.percent]%":
                color "#ffcc00" size 36

    ## --- Key input - desktop ---
    key "a" action Function(_rhythm_state.press_lane, 0)
    key "s" action Function(_rhythm_state.press_lane, 1)
    key "k" action Function(_rhythm_state.press_lane, 2)
    key "l" action Function(_rhythm_state.press_lane, 3)

    ## --- Touch zones - mobile (invisible buttons spanning each lane) ---
    hbox:
        xfill True
        ypos config.screen_height - 200
        spacing 4
        for lane_i in range(4):
            button:
                xfill True
                ysize 200
                background None
                action Function(_rhythm_state.press_lane, lane_i)

    ## --- Continuous update timer ---
    timer 0.016 repeat True action [
        Function(_rhythm_state.update),
        If(_rhythm_state.finished, true=Return())
    ]

    ## --- Lane labels at top ---
    hbox:
        xfill True
        ypos config.screen_height - 100
        spacing 4
        for lane_i in range(4):
            text _rhythm_state.LANE_LABELS[lane_i]:
                xfill True
                xalign 0.5
                size 28
                color _rhythm_state.LANE_COLOURS[lane_i] + "aa"
                textalign 0.5
