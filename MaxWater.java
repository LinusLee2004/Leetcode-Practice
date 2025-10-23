public class MaxWater {
    public int myMaxArea(int[] height) {
        int max = 0;
        for(int i = 0; i < height.length; i++) {
            for(int j = i; j < height.length; j++) {
                int yAxis = Math.min(height[i], height[j]);
                int xAxis = j - i;
                int currentMax = yAxis * xAxis;
                if(currentMax > max) {
                    max = currentMax;
                }
            }
        }
        return max;
    }

    public int maxArea(int[] height) {
        //set pointers to left and right edges of array
        int left = 0;
        int right = height.length - 1;

        //initiate max area variable
        int max = 0;

        //Iterate as long as the left and right pointers haven't reached each other
        while(left < right) {
            int width = right - left;
            int minHeight = Math.min(height[left], height[right]);
            int area = width * minHeight;
            max = Math.max(max, area);

            //Move inward from the shortest height. (If width decreases we cannot possibly be bigger unless height increases.)
            if(height[left] < height[right]) {
                left++;
            }
            else {
                right--;
            }
        }
        return max;
    }
}