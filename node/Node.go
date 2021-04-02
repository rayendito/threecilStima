package node

type Node struct {
	Nama string
	x    int
	y    int
}

func (n Node) GetName() string {
	return n.Nama
}

func (n Node) GetX() int {
	return n.x
}

func (n Node) GetY() int {
	return n.y
}
