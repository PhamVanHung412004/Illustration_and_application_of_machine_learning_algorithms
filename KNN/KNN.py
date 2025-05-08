from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from algorithm import pygame
from algorithm import calc_distance
from algorithm import array_counts
from algorithm import Linear_Search
from algorithm import check_value
from algorithm import Draw_ox_oy
from algorithm import COLORS
from algorithm import colors_init
from algorithm import Show_Mouse
from algorithm import Draw_rect_backgroud
from algorithm import Draw_ox_oy
from algorithm import screen

colors = COLORS()
COLORS_LABELS = colors_init(colors)

class Name_Button:
    def __init__(self,
                 K_Kmeans_button: pygame.surface.Surface,
                dau_cong: pygame.surface.Surface,
                dau_tru: pygame.surface.Surface,
                button_run_kmeans: pygame.surface.Surface,
                k_knn: pygame.surface.Surface,
                run_knn: pygame.surface.Surface,
                deleter_labels: pygame.surface.Surface,
                reset_button: pygame.surface.Surface,
                reset_algorithm: pygame.surface.Surface) -> None:
        self.K_Kmeans_button = K_Kmeans_button
        self.dau_cong = dau_cong
        self.dau_tru = dau_tru
        self.button_run_kmeans = button_run_kmeans
        self.k_knn = k_knn
        self.run_knn = run_knn
        self.deleter_labels = deleter_labels
        self.reset_button = reset_button
        self.reset_algorithm = reset_algorithm
        
            
    def show_name_button(self) -> None: 
        screen.blit(self.K_Kmeans_button,(1230,25))
        screen.blit(self.dau_cong,(1255,80))
        screen.blit(self.dau_tru,(1225 + 80 + 10 + 30 + 5,78)) 
        screen.blit(self.button_run_kmeans,(1230,145))
        screen.blit(self.k_knn,(1250,205))
        screen.blit(self.dau_cong,(1255,260))
        screen.blit(self.dau_tru,(1255 + 100 - 5, 267 - 10)) 

        screen.blit(self.run_knn,(1225 + 30,267 + 60))
        screen.blit(self.deleter_labels,(1225,385))
        screen.blit(self.reset_button,(1270,445))
        screen.blit(self.reset_algorithm,(1260,505))

class Model_KNN:
    def __init__(self, n_KNN: int, 
                datas_train: list[list] = None,
                datas_labels: list[list] = None,
                datas_test: list[list] = None):
        
        self.n_KNN: int = n_KNN
        self.datas_train: list[list] = datas_train
        self.datas_labels: list[list] = datas_labels
        self.datas_test: list[list] = datas_test

    def labels_predict(self) -> np.array:
        model = KNeighborsClassifier(n_neighbors=self.n_KNN)
        model.fit(self.datas_train,self.datas_labels)
        return model.predict(self.datas_test)
        
def Check_and_show(
        labels: list[int],
        value_check: int,
        points: list[int | float | list] = None,
        COLORS_LABELS: COLORS | dict = None) -> None:

    if (type(COLORS_LABELS) == COLORS):
        try:
            for i in range(len(points)):
                pygame.draw.circle(screen,COLORS_LABELS.BLACK,(points[i][0] + 50,600 - points[i][1]),8)
                pygame.draw.circle(screen,COLORS_LABELS.WHITE,(points[i][0] + 50,600 - points[i][1]),7)
        except Exception as e:
            print("Error: {}".format(e))
    else:
        try:
            for i in range(len(labels)):    
                pygame.draw.circle(screen,COLORS_LABELS[labels[i]],(points[i][0] + 50,600 - points[i][1]),7)
        except Exception as e:
            print("Error: {}".format(e))



pygame.init()
test = 0
labels = []
clusters = []
list_labels_news = []
labels_index = []
K_knn = 0
K_Kmeans = 0
results = []
runing = True
points = []

clock = pygame.time.Clock()
font = pygame.font.SysFont('sans', 20)
font1 = pygame.font.SysFont('sans', 30)
font2 = pygame.font.SysFont('sans', 40)
font3 = pygame.font.SysFont('sans', 50) 
check = False



while runing:
    clock.tick(60)
    screen.fill(colors.BACKGROUND)
    x_mouse , y_mouse = pygame.mouse.get_pos()
    
    show_mouse = Show_Mouse(x_mouse, y_mouse, font,colors.BLACK,screen)
    if (50 <= x_mouse <= 1100 and 50 <= y_mouse <= 600):
        show_mouse.show()
    
    x = font.render("X", True, colors.BLACK)
    y = font.render("Y", True, colors.BLACK)
    O = font.render("0", True, colors.BLACK)
    up = font.render("▲", True, colors.BLACK)
    ngang = font.render("►", True, colors.BLACK)
    button_random = font1.render("RANDOM", True, colors.BLACK)
    button_run_kmeans = font1.render("RUN KMEANS", True, colors.BLACK)
    dau_cong = font2.render("+", True, colors.BLACK)
    dau_tru = font2.render("-", True, colors.BLACK)
    run_knn = font1.render("RUN KNN" , True, colors.BLACK)
    deleter_labels = font1.render("DELETE LABEL", True, colors.BLACK)
    reset_button = font1.render("RESET" , True, colors.BLACK)
    reset_algorithm = font1.render("Algorithm" , True, colors.BLACK)
    title = font3.render("Illustration of the k-nearest neighbors algorithm",True,colors.BLACK)

    screen.blit(x, (1100, 605))
    screen.blit(y, (30, 35))
    screen.blit(O, (35, 590))
    screen.blit(title,(200,600))

    # draw ox oy
    draw_ox_oy = Draw_ox_oy(50, 50, 50, 600, 50, 600, 1100, 600, colors.BLACK, up, ngang,screen)
    draw_ox_oy.show()

    #button n_clusters
    rect = Draw_rect_backgroud(1225,20,170,50,colors)
    rect.show()
    # + -
    rect = Draw_rect_backgroud(1225,80,80,50,colors)
    rect.show()
    rect = Draw_rect_backgroud(1225 + 80 + 10,80,80,50,colors)
    rect.show()

    #button random
    rect = Draw_rect_backgroud(1225,140,170,50,colors)
    rect.show()

    #button thuat toan
    rect = Draw_rect_backgroud(1225,200,170,50,colors)
    rect.show()

    #- +
    rect = Draw_rect_backgroud(1225,260,80,50,colors)
    rect.show()
    rect = Draw_rect_backgroud(1225 + 50 + 40,260,80,50,colors)
    rect.show()

    #button RUN KNN
    rect = Draw_rect_backgroud(1225,320,170,50,colors)
    rect.show()

    #button deleter label
    rect = Draw_rect_backgroud(1225,380,170,50,colors)
    rect.show()

    #button reset
    rect = Draw_rect_backgroud(1225,440,170,50,colors)
    rect.show()

    #button Algorithm
    rect = Draw_rect_backgroud(1225,500,170,50,colors)
    rect.show()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = True
            runing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (50 <= x_mouse <= 1100 and 50 <= y_mouse <= 600):
                if (test != 0):
                    list_labels_news.append([x_mouse - 50,abs(y_mouse - 600)])
                else:
                    x = float(x_mouse - 50)
                    y = float(abs(y_mouse - 600))
                    point = [x,y]
                    points.append(point)

            if (1225 <= x_mouse <= 1225 + 170 and 140 <= y_mouse <= 140 + 50):
                print("run kmeans")
                try:
                    test += 1
                    kmeans = KMeans(n_clusters=K_Kmeans).fit(points)
                    labels = kmeans.predict(points)
                    clusters = kmeans.cluster_centers_
                    labels_index = [[points[i],labels[i]] for i in range(len(labels))]

                    # for i in range(len(labels)):
                    #     labels_index.append([points[i],labels[i]])

                except Exception as e:
                    print("Error : {}".format(e))

            if (1225 <= x_mouse <= 1225 + 80 and 80 <= y_mouse <= 80 + 50):
                if (K_Kmeans >= 0 and K_Kmeans < 8):
                    K_Kmeans += 1

            if (1225 + 80 + 10 <= x_mouse <= 1225 + 80 + 10 + 80 and 80 <= y_mouse <= 80 + 50):
                if (0 < K_Kmeans <= 8):
                    K_Kmeans -= 1

            # 1225,260,80,50
            if (1225 <= x_mouse <= 1225 + 80 and 260 < y_mouse <= 260 + 50):
                if (K_knn >= 0 and K_knn < len(points)):
                    K_knn += 1

            # 1225 + 50 + 40,260,80,50
            if (1225 + 50 + 40 <= x_mouse <= 1225 + 50 + 40 + 80 and 260 <= y_mouse <= 260 + 50):
                if (0 < K_knn <= len(points)):
                    K_knn -= 1
            #1225,320,170,50
            if (1225 <= x_mouse <= 1225 + 170 and 320 <= y_mouse <= 320 + 50):
                try:
                    print("Run KNN")                    
                    poins_news = []
                    results = []
                    list_point = []

                    for i in list_labels_news: # O(n)
                        list_distance_labels = []
                        for j in range(len(labels_index)): # O(n)
                            distance = calc_distance(i,labels_index[j][0])
                            list_distance_labels.append([distance,labels_index[j][1]])
                        list_distance_labels.sort() # O(nlog(n))
                        (begin,end,list_counts,labels_distance) = array_counts(list_distance_labels,K_knn) # O(3*n)

                        value_counts = -1
                        list_counts_update = []
                        for index in range(begin,end + 1): # O(m)
                            if (list_counts[index] != 0):
                                list_counts_update.append([list_counts[index],index])
                                value_counts = max(value_counts,list_counts[index])

                        list_index_value_max = Linear_Search(list_counts_update,value_counts) # O(m)
                        labels_distance.sort() # (O(nlog(n)))

                        label = check_value(list_index_value_max,labels_distance) # O(mlog(n))
                        results.append(label) 
                    print("button run: ",results)

                except Exception as e:
                    print("Error: {}".format(e))
                    break
            
            if (1225 <= x_mouse <= 1225 + 170 and 380 <= y_mouse <= 380 + 50):
                try:
                    print("deleter labels")                    
                    list_labels_news = []
                    results = []                    
                except Exception as e:
                    print("Error: {}".format(e))
                    break
                
            # 1225,440,170,50
            if (1225 <= x_mouse <= 1225 + 170 and 440 <= y_mouse <= 440 + 50):
                try: 
                    list_labels_news = []
                    results = []
                    points = []
                    labels_index = []
                    K_knn = 0
                    K_Kmeans = 0
                    test = 0
                    labels = []
                    print("Reset")
                except Exception as e:
                    print("Error: {}".format(e))
                    break
                # 1225,500,170,50
            if (1225 <= x_mouse <= 1225 + 170 and 500 <= y_mouse <= 500 + 50):
                # print("Button Algorithm")
                results = []
                datas_train = [labels_index[i][0] for i in range(len(labels_index))]
                datas_labels = [labels_index[i][1] for i in range(len(labels_index))]
                model = Model_KNN(K_knn,datas_train,datas_labels,list_labels_news)
                results = model.labels_predict()
                print("Button Algorithm",results)

    k_knn = font1.render("K KNN = " + str(K_knn), True, colors.BLACK)
    K_Kmeans_button = font1.render("n_clusters = " + str(K_Kmeans), True, colors.BLACK)               
    name_button = Name_Button(K_Kmeans_button,
                              dau_cong,
                              dau_tru,
                            #   button_random,
                              button_run_kmeans,
                              k_knn,
                              run_knn,
                              deleter_labels,
                              reset_button,
                              reset_algorithm
                              )
    name_button.show_name_button()

    Check_and_show(labels,0,points,colors)
    Check_and_show(labels,1,points,COLORS_LABELS)
    Check_and_show(labels,0,list_labels_news,colors)
    Check_and_show(results,1,list_labels_news,COLORS_LABELS)

    pygame.display.flip()
pygame.quit()
