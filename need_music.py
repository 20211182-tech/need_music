






class Node:
    """노드 클래스: 데이터와 다음 노드 포인터를 저장"""
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    """단순 연결 리스트 클래스"""
    def __init__(self):
        self.head = None
    
    def insert(self, data, position=0):
        """
        연결 리스트에 새로운 항목 추가
        data: 추가할 데이터
        position: 추가 위치 (0=첫 번째, 기본값=첫 번째)
        """
        new_node = Node(data)
        
        # 리스트가 비어있거나 첫 번째 위치에 삽입
        if position == 0 or self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            # 중간 또는 마지막 위치에 삽입
            current = self.head
            for _ in range(position - 1):
                if current.next is None:
                    break
                current = current.next
            new_node.next = current.next
            current.next = new_node
    
    def delete(self, data):
        """
        특정 항목 삭제
        data: 삭제할 데이터
        성공 시 True, 실패 시 False 반환
        """
        if self.head is None:
            return False
        
        # 첫 번째 노드가 삭제할 데이터인 경우
        if self.head.data == data:
            self.head = self.head.next
            return True
        
        # 삭제할 노드 검색
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        
        return False
    
    def get_list(self):
        """
        처음부터 끝까지 순차적으로 가져오는 함수
        리스트의 모든 데이터를 리스트로 반환
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def display(self):
        """리스트 내용 출력 (테스트용)"""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "빈 리스트")


# ===== 테스트 코드 =====
if __name__ == "__main__":
    # 음악 목록 관리
    music_list = linkedlist()
    
    print("=== 음악 목록 관리 ===\n")
    
    #歌曲 추가 (처음에 추가)
    music_list.insert("다시 사랑할 수 있을까")
    print("'다시 사랑할 수 있을까' 추가 (첫 번째)")
    music_list.display()
    
    #歌曲 추가 (마지막에 추가)
    music_list.insert("Dynamite")
    print("\n'Dynamite' 추가 (마지막)")
    music_list.display()
    
    #歌曲 추가 (중간에 삽입)
    music_list.insert("Butter", position=1)
    print("\n'Butter' 추가 (중간)")
    music_list.display()
    
    #歌曲 삭제
    music_list.delete("Dynamite")
    print("\n'Dynamite' 삭제")
    music_list.display()
    
    # get_list()로 모든 항목 가져오기
    print("\n=== get_list() 결과 ===")
    print(music_list.get_list())