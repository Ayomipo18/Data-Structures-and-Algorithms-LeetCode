class Solution {
    public int minMoves(String[] classroom, int energy) {
        /*
        - Min number of moves to collect litter while using/regianing energy state
        - grid travesal with state tracking
        - which state do i wanna track - only moves or moves and energy?
        - I think i want to track both moves and energy and litter
        - I also need to know the no of litter
        - This is a bfs problem
        - Time and Space - O(R x C x 2^L)
        */

        int rows = classroom.length;
        int cols = classroom[0].length();

        int startR = -1;
        int startC = -1;

        List<int[]> litters = new ArrayList<>();

        for(int r=0; r < rows; r++) {
            for(int c=0; c < cols; c++) {
                char ch = classroom[r].charAt(c);
                if (ch == 'S') {
                    startR = r;
                    startC = c;
                } else if (ch == 'L'){
                    litters.add(new int[]{r,c});
                }
            }
        }

        int totalLitters = litters.size();
        int targetMask = (1 << totalLitters) - 1;

        int[][][] maxEnergySeen = new int[rows][cols][1 << totalLitters];

        for(int[][] mat : maxEnergySeen) {
            for(int[] arr : mat) {
                Arrays.fill(arr, -1);
            }
        }

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{startR, startC, energy, 0, 0});
        maxEnergySeen[startR][startC][0] = energy;

        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while(!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];
            int e = curr[2];
            int mask = curr[3];
            int moves = curr[4];

        if (mask == targetMask) {
            return moves;
        }

        if (e == 0) continue;

        for (int[] d : dirs) {
            int nr = r + d[0];
            int nc = c + d[1];
            
            // Boundary check and wall obstacle check ('X')
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || classroom[nr].charAt(nc) == 'X') {
                continue;
            }
            
            int nextEnergy = e - 1;
            int nextMask = mask;
            char nextCell = classroom[nr].charAt(nc);
            
            if (nextCell == 'R') {
                nextEnergy = energy;
            }
            
            if (nextCell == 'L') {
                for (int i = 0; i < totalLitters; i++) {
                    if (litters.get(i)[0] == nr && litters.get(i)[1] == nc) {
                        nextMask |= (1 << i);
                        break;
                    }
                }
            }
            
            if (nextEnergy > maxEnergySeen[nr][nc][nextMask]) {
                maxEnergySeen[nr][nc][nextMask] = nextEnergy;
                queue.offer(new int[]{nr, nc, nextEnergy, nextMask, moves + 1});
            }
        }
    }

    return -1;
    }
}