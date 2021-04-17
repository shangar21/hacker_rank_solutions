#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define MAX 1000

class Graph {
    int* n;
    vector<vector<int>>* edges;
    public:
        Graph(int n) {
            this.n -> n;
            edges -> new vector<vector<int>> edges(n);
        }
    
        void add_edge(int u, int v) {
            edges[*u].push_back(v);
        }
    
        vector<int> shortest_reach(int start) {
            vector<bool> visited(this.n, false);
            vector<int> queue(n);
            vector<int> dist(n);

            visited[start] = true; 
            queue.push_back(start);

            while(!queue.empty()){
                node = queue.front();
                queue.erase(queue.begin());
                for (int i = start; i < edges[start].length(); i++){
                    if (!visited[*i]){
                        visited[*i] = true;
                        dist[*i]++; 
                        queue.push_back(i);
                    }
                }
            }

            vector<int> shortest_reach = {min_element(dist.begin(), dist.end())};

            return shortest_reach;
        }
    
};

int main() {
    int queries;
    cin >> queries;
        
    for (int t = 0; t < queries; t++) {
      
		int n, m;
        cin >> n;
        // Create a graph of size n where each edge weight is 6: 
        Graph graph(n);
        cin >> m;
        // read and set edges
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            u--, v--;
            // add each edge to the graph
            graph.add_edge(u, v);
        }
		int startId;
        cin >> startId;
        startId--;
        // Find shortest reach from node s
        vector<int> distances = graph.shortest_reach(startId);

        for (int i = 0; i < distances.size(); i++) {
            if (i != startId) {
                cout << distances[i] << " ";
            }
        }
        cout << endl;
    }
    
    return 0;
}
