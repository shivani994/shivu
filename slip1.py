Slip1
Q1 Create a simple application which shows the Life cycle of android

MainActivity.java
package com.example.actitvitylifecycle;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

public class MainActivityextendsAppCompatActivity{
String tag="Events";
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);
Log.d(tag, "In on create Event");
    }
public void onStart(){
super.onStart();
Log.d(tag,"InonStart() event");
        }

public void onRestart(){
super.onRestart();
Log.d(tag,"InonRestart() event");
       }

public void onResume(){
super.onResume();
Log.d(tag,"InonResume() event");
      }

public void onPause(){
super.onPause();
Log.d(tag,"InonPause() event");
    }


public void onStop(){
super.onStop();
Log.d(tag,"InonStop() event");
    }


public void onDestroy(){
super.onDestroy();
Log.d(tag,"InonDestroy() event");
    }

}




Q2 Create an android application that demostrateDatePicker and DatePickerDialog

Xml file

<LinearLayout

xmlns:android="http://schemas.android.com/apk/res/android"

xmlns:app="http://schemas.android.com/apk/res-auto"

xmlns:tools="http://schemas.android.com/tools"

android:layout_width="match_parent"

android:layout_height="match_parent"

android:orientation="vertical"

tools:context=".MainActivity">



<Button

android:id="@+id/button"

android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:layout_marginTop="500dp"

android:layout_gravity="center"

android:text="Select Date"/>



<TextView

android:id="@+id/textView"

android:layout_width="match_parent"

android:layout_height="wrap_content"

android:textSize="24sp"

android:layout_gravity="center"/>

</LinearLayout>


Java file

package com.example.slip1datepickerapplication;



import androidx.appcompat.app.AppCompatActivity;



import android.app.DatePickerDialog;

import android.os.Bundle;

import android.view.View;

import android.widget.Button;

import android.widget.DatePicker;

import android.widget.TextView;



import java.util.Calendar;



public class MainActivityextends AppCompatActivity{

private Button button;

private TextViewtextView;



@Override

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

setContentView(R.layout.activity_main);

button = findViewById(R.id.button);

textView= findViewById(R.id.textView);



button.setOnClickListener(new View.OnClickListener() {

@Override

public void onClick(View v) {

DatePickerDialogdatePickerDialog= new DatePickerDialog(MainActivity.this,

new DatePickerDialog.OnDateSetListener() {

@Override

public void onDateSet(DatePickerview, int year, int month, int dayOfMonth) {

String date = dayOfMonth + "/" + (month + 1) + "/" + year;

textView.setText(date);

                            }

                        }, Calendar.getInstance().get(Calendar.YEAR), Calendar.getInstance().get(Calendar.MONTH), Calendar.getInstance().get(Calendar.DAY_OF_MONTH));

datePickerDialog.show();

            }

        });











    }

}


