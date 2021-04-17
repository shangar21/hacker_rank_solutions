struct node {
    
    int data;
    struct node *left;
    struct node *right;
  
};




struct node *lca( struct node *root, int v1, int v2 ) {

	if (v1 < root->data && v2 < root->data){
		lca(root->left, v1,v2);
	}
	else if(v1 > root->data && v2 > root->data){
		lca(root->right,v1,v2);
	}

	return root;

}