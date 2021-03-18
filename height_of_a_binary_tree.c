#define max(a,b) (a>b?a:b)


struct node {
    
    int data;
    struct node *left;
    struct node *right;
  
};

int get_count(struct node* root){

	int count = 0;

	if root == NULL{
		return 0
	}

	return 1 + max(get_count(root->left), get_count(root->right))
}

int getHeight(struct node* root){

	return get_count(root) - 1

}

int main(){
	return 0;
}