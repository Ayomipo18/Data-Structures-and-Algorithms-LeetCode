class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        //two pointer over two sorted lists of intervals
        //p1 and p2
        //if overlap exists in range, green
        //then , if dur in overlap, we move - overlap here is max and min
        //but which pointer moves
        //for p1 to move, we basically check if endtimep1 < endTimep2, p1 is useless to us
        //for p2, we check if endtimep2
        //time - O(n1+n2)
        //space - O(1)

        int p1=0, p2=0;
        int n1 = firstList.length;
        int n2 = secondList.length;
        List<int[]> result = new ArrayList<>();

        while(p1 < n1 && p2 < n2) {
            int maxStartTime = Math.max(firstList[p1][0], secondList[p2][0]);
            int minEndTime = Math.min(firstList[p1][1], secondList[p2][1]);

            if(maxStartTime <= minEndTime) {
                result.add(new int[]{maxStartTime, minEndTime});
            }

            if(firstList[p1][1] < secondList[p2][1]){
                p1++;
            } else {
                p2++;
            }
        }

        return result.toArray(new int[0][]);
    }
}