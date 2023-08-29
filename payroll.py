import datetime
import random
import time
import tkinter.messagebox
from tkinter import *
from tkinter import ttk


class Payroll:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll Management System")
        self.root.geometry("1350x800+0+0")

        notebook = ttk.Notebook(self.root)
        self.Tabcontrol1 = ttk.Frame(notebook)
        self.Tabcontrol2 = ttk.Frame(notebook)
        self.Tabcontrol3 = ttk.Frame(notebook)
        notebook.add(self.Tabcontrol1, text="payroll System")
        notebook.add(self.Tabcontrol2, text="View Payroll")
        notebook.add(self.Tabcontrol3, text="Note Book")
        notebook.grid()

        EmployeeName = StringVar()
        Adress = StringVar()
        Reference = StringVar()
        EmployerName = StringVar()
        CityWeighting = StringVar()
        BasicSalary = StringVar()
        OverTime = StringVar()
        OtherPaymentDue = StringVar()
        GrossPay = StringVar()
        Tax = StringVar()
        Pension = StringVar()
        StudentLoan = StringVar()
        NIPayment = StringVar()
        Deductions = StringVar()
        Gender = StringVar()
        PostCode = StringVar()
        PayDay = StringVar()
        TaxPeriod = StringVar()
        TaxCode = StringVar()
        NINumber = StringVar()
        NICode = StringVar()
        TaxablePay = StringVar()
        PensionablePay = StringVar()
        NetPay = StringVar()

        text_input = StringVar()
        global operator
        operator = ""

        CityWeighting.set("")
        BasicSalary.set("")

        # ======================================Calculator==================================================
        def btnClick(numbers):
            global operator
            operator = operator + str(numbers)
            text_input.set(operator)

        def btnClear():
            global operator
            operator = ""
            text_input.set("")

        def btnEquals():
            global operator
            sumup = str(eval(operator))
            text_input.set(sumup)
            operator = ""

        # =======================================EXIT==========================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Payroll system", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        # ======================================RESET=========================================================
        def iReset():
            EmployeeName.set("")
            Adress.set("")
            Reference.set("")
            EmployerName.set("")
            CityWeighting.set("")
            BasicSalary.set("")
            OverTime.set("")
            GrossPay.set("")
            NetPay.set("")
            Tax.set("")
            Pension.set("")
            StudentLoan.set("")
            NIPayment.set("")
            Deductions.set("")
            PostCode.set("")
            Gender.set("")
            PayDay.set("")
            TaxPeriod.set("")
            NINumber.set("")
            NICode.set("")
            TaxablePay.set("")
            Pension.set("")
            OtherPaymentDue.set("")
            TaxCode.set("")

        # ==================================================PAY====================================================
        def PayRef():
            PayDay.set(time.strftime("%d/%m/%Y"))
            RefPay = random.randint(15000, 90987)
            RefPaid = ("PR" + str(RefPay))
            Reference.set(RefPaid)

            NIpay = random.randint(32000, 578178)
            NIpaid = ("NI" + str(NIpay))
            NINumber.set(NIpaid)

            iDate = datetime.datetime.now()
            TaxPeriod.set(iDate.month)

            NCode = random.randint(1435, 57828)
            CodeNI = ("NIC" + str(NCode))
            NICode.set(CodeNI)

            iTaxCode = random.randint(5783, 28278)
            PaymentTaxCode = ("TCode" + str(iTaxCode))
            TaxCode.set(PaymentTaxCode)

        # ==================================================================================================

        def payment_Function():
            PayRef()

            BS = float(BasicSalary.get())
            CW = float(CityWeighting.get())
            OT = float(OverTime.get())

            MTax = (BS + CW + OT)
            TTax = str('$%.2f'%(MTax))
            Tax.set(TTax)

            M_Pension = ((BS + CW + OT) * 0.02)
            MM_Pension = str("$%.2f" % M_Pension)
            Pension.set(MM_Pension)

            M_StudentLoan = ((BS + CW + OT) * 0.012)
            MM_StudentLoan = str("$%.2f" % M_StudentLoan)
            StudentLoan.set(MM_StudentLoan)

            M_NIPayment = ((BS + CW + OT) * 0.011)
            MM_NIPayment = str("$%.2f" % M_NIPayment)
            StudentLoan.set(MM_NIPayment)

            Deduct = (MTax + M_Pension + M_StudentLoan + M_NIPayment)
            Deduct_Payment = str("$%.2f" % Deduct)
            Deductions.set(Deduct_Payment)
            Gross_Pay = str("$%.2f" % (BS + CW + OT))
            GrossPay.set(Gross_Pay)

            NetPayAfter = (BS + CW + OT) - Deduct
            NetAfter = str("$%.2f" % NetPayAfter)
            NetPay.set(NetAfter)

            TaxablePay.set(TTax)
            PensionablePay.set(MM_Pension)
            OtherPaymentDue.set("0.00")

        # ===================================================================================================

        MainFrame = Frame(self.Tabcontrol1, bd=10, width=1350, height=700, relief=RIDGE)
        MainFrame.grid()
        Tab2Frame = Frame(self.Tabcontrol2, bd=10, width=1350, height=700, relief=RIDGE)
        Tab2Frame.grid()
        Tab3Frame = Frame(self.Tabcontrol3, bd=10, width=1350, height=700, relief=RIDGE)
        Tab3Frame.grid()

        TopFrame1 = Frame(MainFrame, bd=10, width=1340, height=100, relief=RIDGE)
        TopFrame1.grid()
        TopFrame2 = Frame(MainFrame, bd=10, width=1340, height=100, relief=RIDGE)
        TopFrame2.grid()
        TopFrame3 = Frame(MainFrame, bd=10, width=1340, height=500, relief=RIDGE)
        TopFrame3.grid()

        LeftFrame = Frame(TopFrame3, bd=5, width=1340, height=400, padx=2, bg="cadetblue", relief=RIDGE)
        LeftFrame.pack(side=RIGHT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        LeftFrame2 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, bg="cadetblue", relief=RIDGE)
        LeftFrame2.pack(side=TOP)
        LeftFrame2Left = Frame(LeftFrame2, bd=5, width=300, height=170, padx=2, relief=RIDGE)
        LeftFrame2Left.pack(side=LEFT)
        LeftFrame2Right = Frame(LeftFrame2, bd=5, width=300, height=170, padx=2, relief=RIDGE)
        LeftFrame2Right.pack(side=RIGHT)

        LeftFrame3Left = Frame(LeftFrame, bd=5, width=320, height=50, padx=2, relief=RIDGE, bg="cadetblue")
        LeftFrame3Left.pack(side=LEFT)
        LeftFrame3Right = Frame(LeftFrame, bd=5, width=320, height=50, padx=2, relief=RIDGE, bg="cadetblue")
        LeftFrame3Right.pack(side=RIGHT)

        RightFrame1 = Frame(TopFrame3, bd=5, width=320, height=400, padx=2, bg="cadetblue", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=310, height=300, padx=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)
        RightFrame1b = Frame(RightFrame1, bd=5, width=310, height=100, padx=2, relief=RIDGE)
        RightFrame1b.pack(side=TOP)

        RightFrame2 = Frame(TopFrame3, bd=5, width=300, height=400, padx=2, relief=RIDGE, bg="cadetblue")
        RightFrame2.pack(side=LEFT)
        RightFrame2a = Frame(RightFrame2, bd=5, width=280, height=50, padx=2, relief=RIDGE)
        RightFrame2a.pack(side=TOP)
        RightFrame2b = Frame(RightFrame2, bd=5, width=280, height=180, padx=2, relief=RIDGE)
        RightFrame2b.pack(side=TOP)
        RightFrame2c = Frame(RightFrame2, bd=5, width=280, height=100, padx=2, relief=RIDGE)
        RightFrame2c.pack(side=TOP)
        RightFrame2d = Frame(RightFrame2, bd=5, width=280, height=50, padx=2, relief=RIDGE, bg="cadetblue")
        RightFrame2d.pack(side=TOP)

        # =============================================================TILTE=================================

        self.lblTitle = Label(TopFrame1, font=('arial', 40, 'bold'), text="\tPayroll Management System\t",
                              justify=CENTER)
        self.lblTitle.grid(padx=76)

        # =============================================================TILTE=================================

        self.lblEmployeeName = Label(TopFrame2, font=('arial', 12, 'bold'), text="Employee Name", bd=10)
        self.lblEmployeeName.grid(row=0, column=0, sticky=W)
        self.txtEmployeeName = Entry(TopFrame2, font=('arial', 12, 'bold'), bd=5, width=59, justify='left',
                                     textvariable=EmployeeName)
        self.txtEmployeeName.grid(row=0, column=1)

        self.lblAddress = Label(TopFrame2, font=("arial", 12, 'bold'), text="Address", bd=10)
        self.lblAddress.grid(row=1, column=0, sticky=W)
        self.txtAddress = Entry(TopFrame2, font=('arial', 12, 'bold'), bd=5, width=59, justify='left',
                                textvariable=Adress)
        self.txtAddress.grid(row=1, column=1)

        self.lblPostCode = Label(TopFrame2, font=("arial", 12, 'bold'), text="Post Code", bd=5)
        self.lblPostCode.grid(row=0, column=2, sticky=W)
        self.txtPostCode = Entry(TopFrame2, font=('arial', 12, 'bold'), bd=5, width=57, justify='left',
                                 textvariable=PostCode)
        self.txtPostCode.grid(row=0, column=3)

        self.lblGender = Label(TopFrame2, font=("arial", 12, "bold"), text="Gender", bd=10)
        self.lblGender.grid(row=1, column=2, sticky=W)
        self.cboGender = ttk.Combobox(TopFrame2, textvariable=Gender, state='readonly', font=("arial", 14, 'bold'),
                                      width=46)
        self.cboGender['value'] = ('', 'Female', 'Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=1, column=3)

        # ===========================================================================================================
        self.lblPayday = Label(RightFrame2a, font=('arial', 12, 'bold'), text="Payday", bd=10)
        self.lblPayday.grid(row=0, column=0, sticky=W)

        self.txtPayday = Entry(RightFrame2a, font=("arial", 12, "bold"), bd=5, width=19, justify='left',
                               textvariable=PayDay, state=DISABLED)
        self.txtPayday.grid(row=0, column=1)

        self.lblTaxPeriod = Label(RightFrame2b, font=('arial', 12, 'bold'), text="Tax Period", bd=10)
        self.lblTaxPeriod.grid(row=0, column=0, sticky=W)

        self.txtTaxPeriod = Entry(RightFrame2b, font=("arial", 12, "bold"), bd=5, width=16, justify='left',
                                  textvariable=PayDay, state=DISABLED)
        self.txtTaxPeriod.grid(row=0, column=1)

        self.lblTaxCode = Label(RightFrame2b, font=('arial', 12, 'bold'), text="Tax Code", bd=10)
        self.lblTaxCode.grid(row=1, column=0, sticky=W)

        self.txtTaxCode = Entry(RightFrame2b, font=("arial", 12, "bold"), bd=5, width=16, justify='left',
                                textvariable=TaxCode, state=DISABLED)
        self.txtTaxCode.grid(row=1, column=1)

        self.lblNINumber = Label(RightFrame2b, font=('arial', 12, 'bold'), text="NI Number", bd=10)
        self.lblNINumber.grid(row=2, column=0, sticky=W)

        self.txtNINumber = Entry(RightFrame2b, font=("arial", 12, "bold"), bd=5, width=16, justify='left',
                                 textvariable=NINumber, state=DISABLED)
        self.txtNINumber.grid(row=2, column=1)

        self.lblNICode = Label(RightFrame2b, font=('arial', 12, 'bold'), text="NI Code", bd=10)
        self.lblNICode.grid(row=3, column=0, sticky=W)

        self.txtNICode = Entry(RightFrame2b, font=("arial", 12, "bold"), bd=5, width=16, justify='left',
                               textvariable=NICode, state=DISABLED)
        self.txtNICode.grid(row=3, column=1)

        self.lblTaxablePay = Label(RightFrame2c, font=('arial', 12, 'bold'), text="Taxable Pay", bd=10)
        self.lblTaxablePay.grid(row=0, column=0, sticky=W)

        self.txtTaxablePay = Entry(RightFrame2c, font=("arial", 12, "bold"), bd=5, width=11, justify='left',
                                   textvariable=TaxablePay, state=DISABLED)
        self.txtTaxablePay.grid(row=0, column=1)

        self.lblPensioanablePay = Label(RightFrame2c, font=('arial', 12, 'bold'), text="Pensionable Pay", bd=10)
        self.lblPensioanablePay.grid(row=1, column=0, sticky=W)

        self.txtPensionablePay = Entry(RightFrame2c, font=("arial", 12, "bold"), bd=5, width=11, justify='left',
                                       textvariable=PensionablePay, state=DISABLED)
        self.txtPensionablePay.grid(row=1, column=1)

        self.lblNetPay = Label(RightFrame2d, font=('arial', 12, 'bold'), text="Net Pay", bd=10)
        self.lblNetPay.grid(row=0, column=0, sticky=W)

        self.txtNetPay = Entry(RightFrame2d, font=("arial", 12, "bold"), bd=5, width=18, justify='left',
                               textvariable=NetPay, state=DISABLED)
        self.txtNetPay.grid(row=0, column=1)

        # ==========================================================================================================

        self.lblReference = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Refernce", bd=10)
        self.lblReference.grid(row=0, column=0, sticky=W)

        self.txtRefernce = Entry(LeftFrame1, font=("arial", 12, "bold"), bd=5, width=57, justify='left',
                                 textvariable=Reference, state=DISABLED)
        self.txtRefernce.grid(row=0, column=1)

        self.lblEmployerName = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Employer Name", bd=10)
        self.lblEmployerName.grid(row=1, column=0, sticky=W)

        self.txtEmployerName = Entry(LeftFrame1, font=("arial", 12, "bold"), bd=5, width=57, justify='left',
                                     textvariable=EmployerName, state=DISABLED)
        self.txtEmployerName.grid(row=1, column=1)

        self.lblEmployeeName = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Employee Name", bd=10)
        self.lblEmployeeName.grid(row=2, column=0, sticky=W)

        self.txtEmployeeName = Entry(LeftFrame1, font=("arial", 12, "bold"), bd=5, width=57, justify='left',
                                     textvariable=EmployeeName, state=DISABLED)
        self.txtEmployeeName.grid(row=2, column=1)

        # ==================================================================================================
        self.lblCityWeighting = Label(LeftFrame2Left, font=('arial', 12, 'bold'), text="City Weighting", bd=10,
                                      anchor='e')
        self.lblCityWeighting.grid(row=0, column=0, sticky=W)

        self.txtCityWeighting = Entry(LeftFrame2Left, font=("arial", 12, "bold"), bd=5, width=20, justify='left',
                                      textvariable=CityWeighting)
        self.txtCityWeighting.grid(row=0, column=1)

        self.lblBasicSalary = Label(LeftFrame2Left, font=('arial', 12, 'bold'), text="Basic Salary", bd=10)
        self.lblBasicSalary.grid(row=1, column=0, sticky=W)

        self.txtBasicSalary = Entry(LeftFrame2Left, font=("arial", 12, "bold"), bd=5, width=20, justify='left',
                                    textvariable=BasicSalary)
        self.txtBasicSalary.grid(row=1, column=1)

        self.lblOverTime = Label(LeftFrame2Left, font=('arial', 12, 'bold'), text="Over Time", bd=10)
        self.lblOverTime.grid(row=2, column=0, sticky=W)

        self.txtOverTime = Entry(LeftFrame2Left, font=("arial", 12, "bold"), bd=5, width=20, justify='left',
                                 textvariable=OverTime)
        self.txtOverTime.grid(row=2, column=1)

        self.lblOtherPaymentDue = Label(LeftFrame2Left, font=('arial', 12, 'bold'), text="Other Payment", bd=10)
        self.lblOtherPaymentDue.grid(row=3, column=0, sticky=W)

        self.txtOtherPaymentDue = Entry(LeftFrame2Left, font=("arial", 12, "bold"), bd=5, width=20, justify='left',
                                        textvariable=OtherPaymentDue)
        self.txtOtherPaymentDue.grid(row=3, column=1)

        # ==================================================================================================
        self.lblTax = Label(LeftFrame2Right, font=('arial', 12, 'bold'), text="Tax", bd=10, anchor='e')
        self.lblTax.grid(row=0, column=0, sticky=W)

        self.txtTax = Entry(LeftFrame2Right, font=("arial", 12, "bold"), bd=5, width=20, justify='left',
                            textvariable=Tax, state=DISABLED)
        self.txtTax.grid(row=0, column=1)

        self.lblPension = Label(LeftFrame2Right, font=('arial', 12, 'bold'), text="Pension", bd=10)
        self.lblPension.grid(row=1, column=0, sticky=W)

        self.txtPension = Entry(LeftFrame2Right, font=("arial", 12, "bold"), bd=5, width=20, justify='left',
                                textvariable=Pension, state=DISABLED)
        self.txtPension.grid(row=1, column=1)

        self.lblStudentLoan = Label(LeftFrame2Right, font=('arial', 12, 'bold'), text="Student Loan", bd=10)
        self.lblStudentLoan.grid(row=2, column=0, sticky=W)

        self.txtStudentLoan = Entry(LeftFrame2Right, font=("arial", 12, "bold"), bd=5, width=20, justify='left',
                                    textvariable=StudentLoan, state=DISABLED)
        self.txtStudentLoan.grid(row=2, column=1)

        self.lblNIPayment = Label(LeftFrame2Right, font=('arial', 12, 'bold'), text="NI Payment", bd=10)
        self.lblNIPayment.grid(row=3, column=0, sticky=W)

        self.txtNIPayment = Entry(LeftFrame2Right, font=("arial", 12, "bold"), bd=5, width=20, justify='left',
                                  textvariable=NIPayment)
        self.txtNIPayment.grid(row=3, column=1)

        # ==================================================================================================
        self.lblGrossPay = Label(LeftFrame3Left, font=('arial', 12, 'bold'), text="Gross Pay", bd=10)
        self.lblGrossPay.grid(row=0, column=0, sticky=W)

        self.txtGrossPay = Entry(LeftFrame3Left, font=("arial", 12, "bold"), bd=5, width=23, justify='left',
                                 textvariable=GrossPay, state=DISABLED)
        self.txtGrossPay.grid(row=0, column=1)

        self.lblDeductions = Label(LeftFrame3Right, font=('arial', 12, 'bold'), text="Deductions", bd=10)
        self.lblDeductions.grid(row=1, column=0, sticky=W)

        self.txtDeductions = Entry(LeftFrame3Right, font=("arial", 12, "bold"), bd=5, width=23, justify='left',
                                   textvariable=Deductions, state=DISABLED)
        self.txtDeductions.grid(row=1, column=1)

        # ==================================================================================================
        self.txtDisplay = Entry(RightFrame1a, font=("arial", 19, "bold"), bd=5, insertwidth=4, justify='right',
                                textvariable=text_input)
        self.txtDisplay.grid(row=0, column=0, columnspan=4)

        self.btnDigit7 = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="7",
                                command=lambda: btnClick(7))
        self.btnDigit7.grid(row=1, column=0)
        self.btnDigit8 = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="8",
                                command=lambda: btnClick(8))
        self.btnDigit8.grid(row=1, column=1)
        self.btnDigit9 = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="9",
                                command=lambda: btnClick(9))
        self.btnDigit9.grid(row=1, column=2)
        self.btnAdd = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="+",
                             command=lambda: btnClick('+'))
        self.btnAdd.grid(row=1, column=3)

        self.btnDigit4 = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="4",
                                command=lambda: btnClick(4))
        self.btnDigit4.grid(row=2, column=0)
        self.btnDigit5 = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="5",
                                command=lambda: btnClick(5))
        self.btnDigit5.grid(row=2, column=1)
        self.btnDigit6 = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="6",
                                command=lambda: btnClick(6))
        self.btnDigit6.grid(row=2, column=2)
        self.btnSub = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="-",
                             command=lambda: btnClick('-'))
        self.btnSub.grid(row=2, column=3)

        self.btnDigit1 = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="1",
                                command=lambda: btnClick(1))
        self.btnDigit1.grid(row=3, column=0)
        self.btnDigit2 = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="2",
                                command=lambda: btnClick(2))
        self.btnDigit2.grid(row=3, column=1)
        self.btnDigit3 = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="3",
                                command=lambda: btnClick(3))
        self.btnDigit3.grid(row=3, column=2)
        self.btnMulti = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="*",
                               command=lambda: btnClick('*'))
        self.btnMulti.grid(row=3, column=3)

        self.btnDigit0 = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="0",
                                command=lambda: btnClick(0))
        self.btnDigit0.grid(row=4, column=0)
        self.btnClear = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="C",
                               command=lambda: btnClear())
        self.btnClear.grid(row=4, column=1)
        self.btnEquals = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="=",
                                command=lambda: btnEquals())
        self.btnEquals.grid(row=4, column=2)
        self.btnDiv = Button(RightFrame1a, padx=6, pady=6, bd=2, font=("arial", 16, "bold"), width=4, text="/",
                             command=lambda: btnClick('/'))
        self.btnDiv.grid(row=4, column=3)

        self.btnWages = Button(RightFrame1b, padx=16, pady=0, bd=5, font=("arial", 16, "bold"), width=4, text="Wages",
                               command=payment_Function)
        self.btnWages.grid(row=0, column=0)
        self.btnDisplay = Button(RightFrame1b, padx=16, pady=0, bd=5, font=("arial", 16, "bold"), width=4,
                                 text="Display")
        self.btnDisplay.grid(row=0, column=1)
        self.btnUpdate = Button(RightFrame1b, padx=16, pady=0, bd=5, font=("arial", 16, "bold"), width=4, text="Update")
        self.btnUpdate.grid(row=0, column=2)
        self.btnDelete = Button(RightFrame1b, padx=16, pady=0, bd=5, font=("arial", 16, "bold"), width=4, text="Delete",
                                command=PayRef)
        self.btnDelete.grid(row=1, column=0)
        self.btnReset = Button(RightFrame1b, padx=16, pady=0, bd=5, font=("arial", 16, "bold"), width=4, text="Reset",
                               command=iReset)
        self.btnReset.grid(row=1, column=1)
        self.btnExit = Button(RightFrame1b, padx=16, pady=0, bd=5, font=("arial", 16, "bold"), width=4, text="Exit",
                              command=iExit)
        self.btnExit.grid(row=1, column=2)

        # ==================================================================================================
        # ==================================================================================================
        TopFrame11 = Frame(Tab2Frame, bd=10, width=1340, height=100, relief=RIDGE)
        TopFrame11.grid(row=0, column=0)

        TopFrame12 = Frame(Tab2Frame, bd=10, width=1340, height=100, relief=RIDGE)
        TopFrame12.grid(row=1, column=0)

        self.lblTitle = Label(TopFrame11, font=('arial', 40, 'bold'), text="\tPayroll Management System\t", bd=10,
                              justify=CENTER)
        self.lblTitle.grid(padx=72)

        # ========================================================================================================
        scroll_x = Scrollbar(TopFrame12, orient=HORIZONTAL)
        scroll_y = Scrollbar(TopFrame12, orient=VERTICAL)

        self.payroll_records = ttk.Treeview(TopFrame12, height=22, columns=("ref", "fullname", "address",
                                                                            "cityweighting", "basicsalary", "overtime",
                                                                            "grosspay", "tax", "pension", "nipayment",
                                                                            "deductions", "postcode", "gender",
                                                                            "payday",
                                                                            "taxperiod", "taxcode", "ninumber",
                                                                            "netpay"),
                                            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.payroll_records.heading("ref", text="Ref")
        self.payroll_records.heading("fullname", text="Name")
        self.payroll_records.heading("address", text="Address")
        self.payroll_records.heading("cityweighting", text="Cityweighting")

        self.payroll_records.heading("basicsalary", text="Basic Salary")
        self.payroll_records.heading("overtime", text="Overtime")
        self.payroll_records.heading("grosspay", text="GrossPay")
        self.payroll_records.heading("tax", text="Tax")

        self.payroll_records.heading("pension", text="Pension")
        self.payroll_records.heading("nipayment", text="NI Payment")
        self.payroll_records.heading("deductions", text="Deductions")
        self.payroll_records.heading("postcode", text="Post Code")

        self.payroll_records.heading("gender", text="Gender")
        self.payroll_records.heading("payday", text="PayDay")
        self.payroll_records.heading("taxperiod", text="Tax Period")
        self.payroll_records.heading("taxcode", text="Tax Code")
        self.payroll_records.heading("ninumber", text="NI Number")
        self.payroll_records.heading("netpay", text="NetPay")

        self.payroll_records['show'] = 'headings'

        self.payroll_records.column("ref", width=70)
        self.payroll_records.column("fullname", width=70)
        self.payroll_records.column("address", width=120)
        self.payroll_records.column("cityweighting", width=70)
        self.payroll_records.column("basicsalary", width=70)
        self.payroll_records.column("overtime", width=70)
        self.payroll_records.column("grosspay", width=70)
        self.payroll_records.column("tax", width=70)
        self.payroll_records.column("pension", width=70)
        self.payroll_records.column("nipayment", width=70)
        self.payroll_records.column("deductions", width=70)
        self.payroll_records.column("postcode", width=70)
        self.payroll_records.column("gender", width=70)
        self.payroll_records.column("payday", width=70)
        self.payroll_records.column("taxperiod", width=70)
        self.payroll_records.column("taxcode", width=70)
        self.payroll_records.column("ninumber", width=70)
        self.payroll_records.column("netpay", width=70)

        self.payroll_records.pack(fill=BOTH, expand=1)
        self.payroll_records.bind("<ButtonRelease-1>")

        # ========================================================================================================
        TopFrame13 = Frame(Tab3Frame, bd=10, width=1340, height=100, relief=RIDGE)
        TopFrame13.grid(row=0, column=0)
        # ===========================================================================================================
        self.lblNote = Label(TopFrame13, font=("arial", 40, 'bold'), text="\tPayroll Note Book", bd=10, justify=CENTER)
        self.lblNote.grid(row=0, column=0)
        # ==========================================================================================================
        self.txtNote = Text(TopFrame13, font=("arial", 14, 'bold'), width=120, height=22)
        self.txtNote.grid(row=1, column=0)


if __name__ == '__main__':
    root = Tk()
    application = Payroll(root)
    root.mainloop()
