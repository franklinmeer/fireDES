from  multiprocessing import shared_memory

class Automaton:
    def __init__(self, nest, q0, Qm):
        #TODO: Qm eh uma lista
        self.trans = [{}*nest]
        self.q_atual = q0
        self.q0 = q0
        self.Qm = Qm
        self.ef = {}
        self.e_list = []

    def add_event(self, e, f):
        #TODO: evento eh um inteiro
        self.ef[e] = f

    def add_transition(self, qi, e, qf):
        #TODO qi e qf sao inteiros no intervalo [0, nest[
        if self.ef[e]:
            self.trans[qi][e] = qf

    def transition(self, e):
        #TODO: q_atual eh um inteiro
        if self.trans[q_atual][e]:
            self.q_atual = self.trans[q_atual][e]
            return self.ef[e]
        return None


class App_Layer:
    def __init__(self):
        """
        Camada de applicação: automato ->0-a->1-b->0
        a nao controlavel: recebe requisicao
        b controlavel: responde sempre
        """
        self.aut = Automaton(2, 0, [0])

        # Eventos
        self.a = 0
        self.b = 1

        self.aut.add_event(self.a, self.fa)
        self.aut.add_event(self.b, self.fb)
        self.aut.add_transition(0, self.a, 1)
        self.aut.add_transition(1, self.b, 0)

    def fa(self, req):
        print("log: recebeu req: ", req)

    def fb(self, req):
        if req == "ME MANDA A SENHA SECRETA":
            #TODO passar por memoria compartilhada pro proximo layer

            print("legolegal")

    def loop(self):
        #TODO: mem eh uma mmemoria compartilhada
        shm= shared_memory.SharedMemory("mem",True, 256)
        shm.buf="legolegal"
        signal = False
        mem = 0

        if signal:
            f = self.aut.transition(self.a)
            if f:
                f(req)
            f2 = self.aut.transition(self.b)
            if f2:
                f2()

class TCP_SERVER:
    def __init__(self):
        self.aut Automaton(4, 0, [0])
        shm=shared_memory.SharedMemory(name="mem")
        # Eventos
        self.syn = 0
        self.syn_ack= 1
        self.ack= 2
        self.fim= 3

        self.aut.add_event(self.syn, self.f_syn)
        self.aut.add_event(self.syn_ack, self.f_syn_ack)
        self.aut.add_event(self.ack, self.f_ack)
        self.aut.add_event(self.fim, self.f_fim)

        self.aut.add_transition(0, self.syn, 1)
        self.aut.add_transition(1, self.syn_ack, 2)
        self.aut.add_transition(2, self.ack, 3)
        self.aut.add_transition(3, self.fim, 0)

    def f_syn(self):
        print("log: recebeu o syn: ")

    def f_syn_ack(self):
        print("log: envio o syn+ack: ")


    def f_ack(self):
        print("log: recebi o ack: ")

    def f_fim(self):
        print("log: fim da comunicação: ")


    def loop(self):
        #TODO: mem eh uma mmemoria compartilhada

        f = self.aut.transition(self.syn)
            if f:
            f()
        f2 = self.aut.transition(self.syn_ack)
            if f2:
            f2()
        f3 = self.aut.transition(self.ack)
            if f3:
            f3()
        f4 = self.aut.transition(self.fim)
            if f4:
            f4()

class IP:
    def __init__(self):
        self.aut.Automaton()
