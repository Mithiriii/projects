#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>

QString kolej="X";
QString b1="a",b2="b",b3="c",b4="d",b5="e",b6="f",b7="g",b8="h",b9="i";
int ilosc=0;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QString nic=" ";
    ui->kolej_gracza->setText(kolej);
    ui->pushButton_1->setText(nic);
    ui->pushButton_2->setText(nic);
    ui->pushButton_3->setText(nic);
    ui->pushButton_4->setText(nic);
    ui->pushButton_5->setText(nic);
    ui->pushButton_6->setText(nic);
    ui->pushButton_7->setText(nic);
    ui->pushButton_8->setText(nic);
    ui->pushButton_9->setText(nic);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_wyjdz_clicked()
{
    MainWindow::close();
}

void MainWindow::on_pushButton_1_clicked()
{
    if(ui->pushButton_1->text()==" "){
        ui->pushButton_1->setText(kolej);
        b1=kolej;
        if(kolej=="X"){
            kolej="O";
        }
        else{
            kolej="X";
        }
        ui->kolej_gracza->setText(kolej);\
        ilosc++;
        sprawdz();
    }
}




void MainWindow::on_pushButton_2_clicked()
{
    if(ui->pushButton_2->text()==" "){
        ui->pushButton_2->setText(kolej);
        b2=kolej;
        if(kolej=="X"){
            kolej="O";
        }
        else{
            kolej="X";
        }
        ui->kolej_gracza->setText(kolej);
        ilosc++;
        sprawdz();
    }
}

void MainWindow::on_pushButton_3_clicked()
{
    if(ui->pushButton_3->text()==" "){
        ui->pushButton_3->setText(kolej);
        b3=kolej;
        if(kolej=="X"){
            kolej="O";
        }
        else{
            kolej="X";
        }
        ui->kolej_gracza->setText(kolej);
        ilosc++;
        sprawdz();
    }
}

void MainWindow::on_pushButton_4_clicked()
{
    if(ui->pushButton_4->text()==" "){
        ui->pushButton_4->setText(kolej);
        b4=kolej;
        if(kolej=="X"){
            kolej="O";
        }
        else{
            kolej="X";
        }
        ui->kolej_gracza->setText(kolej);
        sprawdz();
    }
}

void MainWindow::on_pushButton_5_clicked()
{
    if(ui->pushButton_5->text()==" "){
        ui->pushButton_5->setText(kolej);
        b5=kolej;
        if(kolej=="X"){
            kolej="O";
        }
        else{
            kolej="X";
        }
        ui->kolej_gracza->setText(kolej);
        ilosc++;
        sprawdz();
    }
}

void MainWindow::on_pushButton_6_clicked()
{
    if(ui->pushButton_6->text()==" "){
        ui->pushButton_6->setText(kolej);
        b6=kolej;
        if(kolej=="X"){
            kolej="O";
        }
        else{
            kolej="X";
        }
        ui->kolej_gracza->setText(kolej);
        ilosc++;
        sprawdz();
    }
}

void MainWindow::on_pushButton_7_clicked()
{
    if(ui->pushButton_7->text()==" "){
        ui->pushButton_7->setText(kolej);
        b7=kolej;
        if(kolej=="X"){
            kolej="O";
        }
        else{
            kolej="X";
        }
        ui->kolej_gracza->setText(kolej);
        ilosc++;
        sprawdz();
    }
}

void MainWindow::on_pushButton_8_clicked()
{
    if(ui->pushButton_8->text()==" "){
        ui->pushButton_8->setText(kolej);
        b8=kolej;
        if(kolej=="X"){
            kolej="O";
        }
        else{
            kolej="X";
        }
        ui->kolej_gracza->setText(kolej);
        ilosc++;
        sprawdz();
    }
}

void MainWindow::on_pushButton_9_clicked()
{
    if(ui->pushButton_9->text()==" "){
        ui->pushButton_9->setText(kolej);
        b9=kolej;
        if(kolej=="X"){
            kolej="O";
        }
        else{
            kolej="X";
        }
        ui->kolej_gracza->setText(kolej);
        ilosc++;
        sprawdz();
    }
}

void MainWindow::sprawdz()
 {
    if((b1==b2 && b2==b3 && b1!=" ") ||
       (b4==b5 && b5==b6 && b4!=" ") ||
       (b7==b8 && b8==b9 && b7!=" ") ||
       (b1==b4 && b4==b7 && b7!=" ") ||
       (b2==b5 && b5==b8 && b2!=" ") ||
       (b3==b6 && b6==b9 && b3!=" ") ||
       (b1==b5 && b5==b9 && b1!=" ") ||
       (b3==b5 && b5==b7 && b3!=" "))
    {
       if (kolej=="X"){
           QMessageBox msgBox;
           msgBox.setWindowTitle("Koniec gry!!");
           msgBox.setText("Kolko wygralo.");
           msgBox.exec();
       }
       else{
           QMessageBox msgBox;
           msgBox.setWindowTitle("Koniec gry!!");
           msgBox.setText("Krzyzyk wygral.");
           msgBox.exec();
       }
       ui->pushButton_1->setText(" ");
       ui->pushButton_2->setText(" ");
       ui->pushButton_3->setText(" ");
       ui->pushButton_4->setText(" ");
       ui->pushButton_5->setText(" ");
       ui->pushButton_6->setText(" ");
       ui->pushButton_7->setText(" ");
       ui->pushButton_8->setText(" ");
       ui->pushButton_9->setText(" ");
        b1="a";
        b2="b";
        b3="c";
        b4="d";
        b5="e";
        b6="f";
        b7="g";
        b8="h";
        b9="i";
        ilosc=0;
    }
    else if(ilosc==8){
        QMessageBox msgBox;
        msgBox.setWindowTitle("Koniec gry!!");
        msgBox.setText("Remis.");
        msgBox.exec();
        ui->pushButton_1->setText(" ");
        ui->pushButton_2->setText(" ");
        ui->pushButton_3->setText(" ");
        ui->pushButton_4->setText(" ");
        ui->pushButton_5->setText(" ");
        ui->pushButton_6->setText(" ");
        ui->pushButton_7->setText(" ");
        ui->pushButton_8->setText(" ");
        ui->pushButton_9->setText(" ");
         b1="a";
         b2="b";
         b3="c";
         b4="d";
         b5="e";
         b6="f";
         b7="g";
         b8="h";
         b9="i";
         ilosc=0;
    }
 }
