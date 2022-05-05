#-*-coding:utf8;-*-
#qpy:console

head = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
	android:layout_width="fill_parent"
	android:layout_height="fill_parent"
	android:background="#ff000000"
	android:orientation="vertical"
	xmlns:android="http://schemas.android.com/apk/res/android">
"""

tail = """
<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="8">
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="1"
			android:id="@+id/but1"
			android:textSize="8dp"
			android:background="#ffffffff"
			android:textColor="#ff000000"
			android:layout_weight="1"
			android:gravity="center"/>
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="2"
			android:id="@+id/but2"
			android:textSize="8dp"
			android:background="#ffdcdcdc"
			android:textColor="#ff000000"
			android:layout_weight="1"
			android:gravity="center"/>
			<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="3"
			android:id="@+id/but3"
			android:textSize="8dp"
			android:background="#ffffffff"
			android:textColor="#ff000000"
			android:layout_weight="1"
			android:gravity="center"/>
	</LinearLayout>
		<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="8">
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="4"
			android:id="@+id/but4"
			android:textSize="8dp"
			android:background="#ffdcdcdc"
			android:textColor="#ff000000"
			android:layout_weight="1"
			android:gravity="center"/>
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="5"
			android:id="@+id/but5"
			android:textSize="8dp"
			android:background="#ffffffff"
			android:textColor="#ff000000"
			android:layout_weight="1"
			android:gravity="center"/>
			<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="6"
			android:id="@+id/but6"
			android:textSize="8dp"
			android:background="#ffdcdcdc"
			android:textColor="#ff000000"
			android:layout_weight="1"
			android:gravity="center"/>
	</LinearLayout>
	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="8">
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="7"
			android:id="@+id/but7"
			android:textSize="8dp"
			android:background="#ffffffff"
			android:textColor="#ff000000"
			android:layout_weight="1"
			android:gravity="center"/>
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="8"
			android:id="@+id/but8"
			android:textSize="8dp"
			android:background="#ffdcdcdc"
			android:textColor="#ff000000"
			android:layout_weight="1"
			android:gravity="center"/>
			<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="9"
			android:id="@+id/but9"
			android:textSize="8dp"
			android:background="#ffffffff"
			android:textColor="#ff000000"
			android:layout_weight="1"
			android:gravity="center"/>
	</LinearLayout>
	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="8">
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="+-"
			android:id="@+id/chetnechet"
			android:textSize="8dp"
			android:background="#ffEFC802"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="Calculate"
			android:id="@+id/calculate"
			android:textSize="8dp"
			android:background="#ff000000"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="Diagonal"
			android:id="@+id/diag"
			android:textSize="8dp"
			android:background="#ffff0000"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>
	</LinearLayout>
		</LinearLayout>
</LinearLayout>
"""

def makebutton(i,j):
    name = "f"+str(i)+"x"+str(j)
    begin = """<Button
			android:layout_width="40dp"
			android:layout_height="40dp"
			android:text=""
			android:id="@+id/"""
    end = """"
			android:background="#ffffffff"
			android:textColor="#ff000000"
			android:layout_weight="1"
			android:textSize="7dp"
			android:gravity="center"
			android:layout_marginBottom="1dp"
			"""
    if i % 3 == 0 and i != 0:
        end += """android:layout_marginTop="1dp"
        """
    if j != 0:
        if j % 3 == 0:
            end += """android:layout_marginLeft="2dp"
            """
        else:
            end += """android:layout_marginLeft="1dp"
        """
    end += "/>"
    return begin+name+end

line = """
<LinearLayout
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:orientaton="horizontal"
		android:layout_gravity="center">"""
close = """</LinearLayout>"""
point = """<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="3"
			android:id="@+id/but3"
			android:textSize="8dp"
			android:background="#ff06AF00"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>"""


def createfield(n,m):
    field = ""
    for i in range(n):
        field += line
        for j in range(m):
            field += makebutton(i,j)
        field += close
    return field

fv = open("fieldview.txt","w")
fld = createfield(9,9)
fv.write(fld)
fv.close()
mv = open("mainview.txt","w")
mv.write(head+fld+tail)
mv.close()

