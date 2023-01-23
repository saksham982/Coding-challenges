import java.util.*;

public class MergeSort_2330544 {
    //creating a getInput method where the values are added to the arraylist by the user
    ArrayList<Integer> getInput(ArrayList<Integer> al) {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter the number of elements you want");
        int a=s.nextInt();
        for(int i=0;i<a;i++){
            System.out.println("Enter the integer element");
            //applying try and catch to prevent user from entering string data
            try{
                al.add(s.nextInt());}
            catch(Exception e){
                System.out.println("Sorry only integer is accepted. Please try again.");
                s.next();//to reset the invalid input
                i--;//decrementing to allow the user another try
            }

        } return al;//returning the value of ArrayList named al
    }
    //creating another method getOutput to display the unsorted and sorted array
    void getOutput(ArrayList<Integer> al,String listCondition) {//adding string type in parameter to return either Unosrted or Sorted msg
        System.out.println(listCondition);
        System.out.println(al);
    }
    //creating merge method to merge the two sorted arrays
    void merge(ArrayList<Integer> al, int beg, int mid, int end) {
        int leftside = beg;
        int rightside= mid + 1;
        ArrayList<Integer> temp = new ArrayList<>();// creating a temporary arraylist to store the sorted list
        while (leftside <= mid && rightside <= end) {
            if (al.get(leftside) < al.get(rightside)) {
                temp.add(al.get(leftside));
                leftside++;
            } else {
                temp.add(al.get(rightside));
                rightside++;
            }
        }
        while (leftside <= mid) {
            temp.add(al.get(leftside));
            leftside++;
        }
        while (rightside <= end) {
            temp.add(al.get(rightside));
            rightside++;
        }
        for (int i = 0; i < temp.size(); i++) {
            al.set(beg + i, temp.get(i));
        }
    }
    //creating sort method to  sort and merge the elemnts of arrays until no more division is possible
    void sort(ArrayList<Integer> al, int beg, int end) {
        if (beg<end) {
            int mid = (beg + end) / 2;
            sort(al, beg, mid);
            sort(al, mid + 1, end);
            merge(al, beg, mid, end);
        }
    }
    // creating a main method where object ab is defined to call and use the above methods.
    public static void main(String[] args) {
        MergeSort_2330544 ab = new MergeSort_2330544();
        ArrayList<Integer> al = ab.getInput(new ArrayList<Integer>());
        ab.getOutput(al,"Unsorted list");
        ab.sort(al, 0, al.size() - 1);
        ab.getOutput(al,"Sorted list");
    }
}
