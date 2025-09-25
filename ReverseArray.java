public class ReverseArray {
    public int[] revArr(int[] arr) {
        int[] rev = new int[arr.length];
        for(int i = 0; i < arr.length; i++){
            rev[arr.length - 1 - i] = arr[i];
        }
        return rev;
    }
}
