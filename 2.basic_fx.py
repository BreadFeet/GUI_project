from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox

root = Tk()
root.title("프로젝트")

# 파일 프레임
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5)

def add_file() :
    files = filedialog.askopenfilenames(title="Select image files",\
        filetypes=(("PNG file", "*.png"), ("All files", "*.*")),\
        initialdir=r"C:\Users\sori-\OneDrive\문서\Certi. Marketing\417")   

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
path_frame = LabelFrame(root, text="Storage path")
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
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(option_frame, state="readonly", values=opt_width, width=10)
cmb_width.current(0)        # index: 0 값을 자동으로 세팅
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
lbl_gap = Label(option_frame, text="Gap", width=5)
lbl_gap.pack(side="left", padx=5, pady=5)
# 콤보박스
opt_gap = ["없음", "좁게", "보통", "넓게"]
cmb_gap = ttk.Combobox(option_frame, state="readonly", values=opt_gap, width=6)
cmb_gap.current(0)
cmb_gap.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
lbl_form = Label(option_frame, text="Format", width=6)
lbl_form.pack(side="left", padx=5, pady=5)
# 콤보박스
opt_form = ["jpg", "png", "bnp"]
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

def start() :  # 각 옵션을 가져와야 함
    print("width: {}".format(cmb_width.get()))
    print("gap:", cmb_gap.get())
    print("format: ", cmb_form.get())

    # 파일 목록 유무 확인
    if list_file.size() == 0 :
        msgbox.showwarning("Warning", "Please select image files !")
        return

    # 저장 경로 유무 확인
    if len(txt_path.get()) == 0 :
        msgbox.showwarning("Warning", "Please select a folder to save file !")
        return

btn_start = Button(run_frame, padx=30, pady=5, text="Start", command=start)
btn_start.pack(side="right", padx=5, pady=5)


 

root.resizable(False, False)
root.mainloop() 