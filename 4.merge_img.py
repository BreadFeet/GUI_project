from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image
import os

root = Tk()
root.title("Make it One !")

# 파일 프레임
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5)

def add_file() :
    files = filedialog.askopenfilenames(title="Select image files",\
        filetypes=(("PNG file", "*.png"), ("All files", "*.*")),\
        initialdir=r"C:\Users\sori-\Desktop\PythonWorkSpace")   

    # 사용자가 선택한 파일목록을 terminal에 출력
    for file in files :
        list_file.insert(END, file)

btn_add_file = Button(file_frame, padx=20, pady=5, text ="Add file", command=add_file)
btn_add_file.pack(side="left")

def del_file() :
    for i in reversed(list_file.curselection()) :
        list_file.delete(i)

btn_del_file = Button(file_frame, padx=20, pady=5, text="Select deletion", command=del_file)
btn_del_file.pack(side="right")

# 리스트박스 & 스크롤바 & 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)    # 프레임이 공간 차도록 함(otherwise, 안참)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)

scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="Directory")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_path = Entry(path_frame)
txt_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5)  # 입력창 안쪽높이 변경


def save_file() :     # 파일X, 폴더 열기
    folder_selected = filedialog.askdirectory()
    if folder_selected == None :     # 사용자가 취소를 누를 때
        return
    # 사용자 선택 경로를 entry 안에 넣기
    txt_path.delete(0, END)          # 기존 경로 있으면 지우기
    txt_path.insert(0, folder_selected)
    
btn_path = Button(path_frame, text="Save as", width=10, command=save_file)
btn_path.pack(side="right", padx=5 , pady=5)


# 옵션 프레임
option_frame = LabelFrame(root, text="Option")
option_frame.pack(padx=5, pady=5, ipady=5)

# 1. 가로넢이 옵션 (이름-콤보박스)
lbl_width = Label(option_frame, text="Width", width=5)
lbl_width.pack(side="left", padx=5, pady=5)
# 콤보박스 만들기 위해서 위에 ttk 불러와야 함!
opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(option_frame, state="readonly", values=opt_width, width=10)
cmb_width.current(0)        # index: 0 값을 자동으로 세팅
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
lbl_gap = Label(option_frame, text="Gap", width=5)
lbl_gap.pack(side="left", padx=5, pady=5)
# 콤보박스
opt_gap = ["None", "Narrow", "Normal", "Wide"]
cmb_gap = ttk.Combobox(option_frame, state="readonly", values=opt_gap, width=6)
cmb_gap.current(0)
cmb_gap.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
lbl_form = Label(option_frame, text="Format", width=6)
lbl_form.pack(side="left", padx=5, pady=5)
# 콤보박스
opt_form = [".jpg", ".png", ".bnp"]
cmb_form = ttk.Combobox(option_frame, state="readonly", values=opt_form, width=6)
cmb_form.current(0)
cmb_form.pack(side="left", padx=5, pady=5)


# 진행 상황 - 프로그레스 바
pgbar_frame = LabelFrame(root, text="Progress")
pgbar_frame.pack(fill="x", padx=5, pady=5, ipady=5)

pgbar_var = DoubleVar()
pgbar = ttk.Progressbar(pgbar_frame, maximum=100, variable=pgbar_var)
pgbar.pack(fill="x", padx=5, pady=5)


# 실행 프레임
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

# 가장 오른쪽에 나와야 할 버튼 부터 순서대로 작성해야!
btn_close = Button(run_frame, padx=30, pady=5, text="Close", command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)


    # merge_image 함수 정의
def merge_image() :
    img = [Image.open(x) for x in list_file.get(0, END)]  # 리스트에 저장된 글자를 이미지로 인식
    # width = [x.size[0] for x in img] 
    # height =[x.size[1] for x in img]
    width, height = zip(*{x.size for x in img})
    print(list(x.size for x in img))   # [(10,10), (20,20)] 처럼 출력 확인

    max_width, total_height = max(width), sum(height)   # 튜플

    # 스케치북 준비
    final_img = Image.new("RGB", (max_width, total_height), (255, 255, 255)) 
                          # "RGB",  (가로크기, 세로크기), 흰색배경 RGB 값
    y_offset = 0        # 사진이 붙을 y 위치
    # for pic in img :
    #     final_img.paste(pic, (0, y_offset))     # (가져올 사진, 위치)
    #     y_offset += pic.size[1]     # 삽입된 이미지의 height만큼 y 위치 이동

    # 프로그레스바 세팅
    for count, pic in enumerate(img) :     
      # 위와 img에서 pic 선택하는 것은 같지만, count를 추가할 수 있음
        final_img.paste(pic, (0, y_offset))
        y_offset += pic.size[1]

        progress = (count + 1) / len(img) * 100    # 진행 퍼센트 계산
        pgbar_var.set(progress)                    # 진행 퍼센트만큼 바 생성
        pgbar.update()

    # 지정 경로에 저장시키기
    save_path = os.path.join(txt_path.get(), "Sori's outcome.jpg")   # (저장위치, 저장이름)
    final_img.save(save_path)      # 이미지 저장 경로 지정
    msgbox.showinfo("Notification", "Process finished.")


def start() :  # 각 옵션값을 terminal에 출력
    # print("width: {}".format(cmb_width.get()))
    # print("gap:", cmb_gap.get())
    # print("format: ", cmb_form.get())

    # 파일 목록 유무 확인
    if list_file.size() == 0 :
        msgbox.showwarning("Warning", "Please select image files !")
        return

    # 저장 경로 유무 확인
    if len(txt_path.get()) == 0 :
        msgbox.showwarning("Warning", "Please select a folder to save file !")
        return

    # 이미지 통합 작업
    merge_image()

btn_start = Button(run_frame, padx=30, pady=5, text="Start", command=start)
btn_start.pack(side="right", padx=5, pady=5)


 

root.resizable(False, False)
root.mainloop() 