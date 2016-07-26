import numpy as np
import pylab as plt

# programme permettant de lire les courbes de lumieres des Supernovas SNLS de JLA

listSN=['lc-06D4dh.list', 'lc-06D4cq.list','lc-06D4co.list','lc-06D4cl.list','lc-06D4ce.list','lc-06D4bw.list','lc-06D4bo.list','lc-06D4ba.list','lc-06D3gx.list','lc-06D3gn.list','lc-06D3gh.list','lc-06D3fp.list','lc-06D3et.list','lc-06D3en.list','lc-06D3em.list','lc-06D3el.list','lc-06D3ed.list','lc-06D3dt.list','lc-06D3do.list','lc-06D3df.list','lc-06D3cc.list','lc-06D3bz.list','lc-06D2gb.list','lc-06D2ga.list','lc-06D2fb.list','lc-06D2ck.list','lc-06D2ce.list','lc-06D2cd.list','lc-06D2cc.list','lc-06D2ca.list','lc-06D2bk.list','lc-05D4hn.list','lc-05D4gw.list','lc-05D4fo.list','lc-05D4fg.list','lc-05D4ff.list','lc-05D4ev.list','lc-05D4ek.list','lc-05D4ej.list','lc-05D4ef.list','lc-05D4dy.list','lc-05D4dw.list','lc-05D4dt.list','lc-05D4cw.list','lc-05D4cs.list','lc-05D4cq.list','lc-05D4cn.list','lc-05D4bm.list','lc-05D4bj.list','lc-05D4bi.list','lc-05D4bf.list','lc-05D4be.list','lc-05D4av.list','lc-05D4ag.list','lc-05D4af.list','lc-05D3ne.list','lc-05D3mx.list','lc-05D3mq.list','lc-05D3mn.list','lc-05D3mh.list','lc-05D3lr.list','lc-05D3lc.list','lc-05D3lb.list','lc-05D3la.list','lc-05D3kx.list','lc-05D3kt.list','lc-05D3kp.list','lc-05D3km.list','lc-05D3jr.list','lc-05D3jq.list','lc-05D3jk.list','lc-05D3jh.list','lc-05D3jb.list','lc-05D3ht.list','lc-05D3hs.list','lc-05D3hh.list','lc-05D3ha.list','lc-05D3gv.list','lc-05D3gp.list','lc-05D3dh.list','lc-05D3dd.list','lc-05D3cx.list','lc-05D3cq.list','lc-05D3ci.list','lc-05D3cf.list','lc-05D3ax.list','lc-05D2ob.list','lc-05D2nt.list','lc-05D2nn.list','lc-05D2my.list','lc-05D2mp.list','lc-05D2le.list','lc-05D2ie.list','lc-05D2he.list','lc-05D2hc.list','lc-05D2fq.list','lc-05D2ec.list','lc-05D2eb.list','lc-05D2dy.list','lc-05D2dw.list','lc-05D2dt.list','lc-05D2ct.list','lc-05D2ck.list','lc-05D2ci.list','lc-05D2cb.list','lc-05D2by.list','lc-05D2bw.list','lc-05D2bv.list','lc-05D2bt.list','lc-05D2ay.list','lc-05D2ah.list','lc-05D2ac.list','lc-05D2ab.list','lc-05D1kl.list','lc-05D1ke.list','lc-05D1iz.list','lc-05D1ix.list','lc-05D1if.list','lc-05D1hm.list','lc-05D1hk.list','lc-05D1er.list','lc-05D1eo.list','lc-05D1em.list','lc-05D1ee.list','lc-05D1dx.list','lc-05D1dn.list','lc-05D1cl.list','lc-05D1ck.list','lc-05D1cc.list','lc-05D1cb.list','lc-05D1az.list','lc-04D4jy.list','lc-04D4jw.list','lc-04D4ju.list','lc-04D4jr.list','lc-04D4in.list','lc-04D4im.list','lc-04D4ii.list','lc-04D4ih.list','lc-04D4id.list','lc-04D4ic.list','lc-04D4ib.list','lc-04D4hu.list','lc-04D4hf.list','lc-04D4gg.list','lc-04D4fx.list','lc-04D4dw.list','lc-04D4dm.list','lc-04D4bq.list','lc-04D4bk.list','lc-04D4an.list','lc-04D3oe.list','lc-04D3ny.list','lc-04D3nr.list','lc-04D3nh.list','lc-04D3nc.list','lc-04D3ml.list','lc-04D3mk.list','lc-04D3lu.list','lc-04D3lp.list','lc-04D3ks.list','lc-04D3kr.list','lc-04D3hn.list','lc-04D3gx.list','lc-04D3gt.list','lc-04D3fq.list','lc-04D3fk.list','lc-04D3ez.list','lc-04D3do.list','lc-04D3df.list','lc-04D3dd.list','lc-04D3cy.list','lc-04D3co.list','lc-04D2mj.list','lc-04D2mh.list','lc-04D2mc.list','lc-04D2kr.list','lc-04D2ja.list','lc-04D2iu.list','lc-04D2gp.list','lc-04D2gc.list','lc-04D2gb.list','lc-04D2fs.list','lc-04D2fp.list','lc-04D2cf.list','lc-04D2an.list','lc-04D2al.list','lc-04D1sk.list','lc-04D1si.list','lc-04D1sa.list','lc-04D1rx.list','lc-04D1rh.list','lc-04D1qd.list','lc-04D1pu.list','lc-04D1pp.list','lc-04D1pg.list','lc-04D1pd.list','lc-04D1pc.list','lc-04D1ow.list','lc-04D1oh.list','lc-04D1ks.list','lc-04D1kj.list','lc-04D1jg.list','lc-04D1jd.list','lc-04D1iv.list','lc-04D1hy.list','lc-04D1hx.list','lc-04D1hd.list','lc-04D1ff.list','lc-04D1de.list','lc-04D1dc.list','lc-04D1aj.list','lc-03D4gg.list','lc-03D4gf.list','lc-03D4fd.list','lc-03D4dy.list','lc-03D4di.list','lc-03D4dh.list','lc-03D4cz.list','lc-03D4cy.list','lc-03D4cx.list','lc-03D4cj.list','lc-03D4au.list','lc-03D4at.list','lc-03D4ag.list','lc-03D3cd.list','lc-03D3bl.list','lc-03D3ba.list','lc-03D3ay.list','lc-03D3aw.list','lc-03D1fq.list','lc-03D1fc.list','lc-03D1ew.list','lc-03D1dt.list','lc-03D1co.list','lc-03D1bp.list','lc-03D1ax.list','lc-03D1aw.list','lc-03D1au.list']


def save_pkl(obj, name):
    with open( name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_pkl(name):
    with open( name, 'rb') as f:
        return pickle.load(f)


def read_list(list_file, SkipRows=1, delimiteur=' '):
    LISTFILE=np.loadtxt(list_file, dtype='string', unpack=True,delimiter=delimiteur,skiprows=SkipRows)
    data_string=LISTFILE[0:]
    return data_string


def convert(data_string):
    data=np.zeros(np.shape(data_string))
    print np.shape(data_string), len(data[:,0]),len(data[0])
    for i in range(len(data[:,0])):
        for j in range(len(data[0])):
            if data_string[i,j] != '':
                data[i,j]=float(data_string[i,j])
            else:
                # data[i,j]=N.nan
                continue
    return data


def create_dico_for_one_sn(data_string):
    dic_sn={}
    for i in range(len(data_string[4])):
        dic_sn[data_string[4][i]]={}
        dic_sn[data_string[4][i]]['Date']=[]
        dic_sn[data_string[4][i]]['Flux']=[]
        dic_sn[data_string[4][i]]['Fluxerr']=[]
        dic_sn[data_string[4][i]]['ZP']=[]
        dic_sn[data_string[4][i]]['end']=[] # ?
    for i in range(len(data_string[0])):
        dic_sn[data_string[4][i]]['Date'].append(float(data_string[0][i]))
        dic_sn[data_string[4][i]]['Flux'].append(float(data_string[1][i]))
        dic_sn[data_string[4][i]]['Fluxerr'].append(float(data_string[2][i]))
        dic_sn[data_string[4][i]]['ZP'].append(float(data_string[3][i]))
        dic_sn[data_string[4][i]]['end'].append(data_string[4][i])
    return dic_sn


def ajouter_entete(dic_sn,snls_sn):
    path_input = snls_sn
    input_file = open(path_input, "r")
    line = 'initiation lecture lignes'
    dic_sn['SN_name']=snls_sn
    while line:
        line = input_file.readline()
        splittedString = line.split('@')
        splittedString=''.join(splittedString)
        splittedString = splittedString.split('\n')
        splittedString=''.join(splittedString)
        splittedString = splittedString.split(' ')
        if '#' in splittedString[0]:
            break
        dic_sn[splittedString[0]]=splittedString[1:]
        if (len(dic_sn[splittedString[0]])==1):
            dic_sn[splittedString[0]]=splittedString[1]
       # print 'dic_sn[splittedString[0]]', dic_sn[splittedString[0]]
    input_file.close()


def plot_snls_light_curve(dic, snls_sn, couleurs=['g','r','i','z']):
 
    dict_sn = dic[snls_sn]
    if 'g' in couleurs:
        plt.errorbar(dict_sn['MEGACAMPSF::g']['Date'], dict_sn['MEGACAMPSF::g']['Flux'], xerr=None, yerr=dict_sn['MEGACAMPSF::g']['Fluxerr'],linestyle='',alpha=0.75, marker='o', color='g', label='g')
    if 'r' in couleurs:
        plt.errorbar(dict_sn['MEGACAMPSF::r']['Date'], dict_sn['MEGACAMPSF::r']['Flux'], xerr=None, yerr=dict_sn['MEGACAMPSF::r']['Fluxerr'],linestyle='',alpha=0.75, marker='o', color='r', label="r")
    if 'i' in couleurs:
        plt.errorbar(dict_sn['MEGACAMPSF::i']['Date'], dict_sn['MEGACAMPSF::i']['Flux'], xerr=None, yerr=dict_sn['MEGACAMPSF::i']['Fluxerr'],linestyle='',alpha=0.75, marker='o', color='k', label='i')
    if 'z' in couleurs:
        plt.errorbar(dict_sn['MEGACAMPSF::z']['Date'], dict_sn['MEGACAMPSF::z']['Flux'], xerr=None, yerr=dict_sn['MEGACAMPSF::z']['Fluxerr'],linestyle='',alpha=0.75, marker='o', color='b', label='z')
    plt.legend()
    plt.title('Courbe de lumiere ' + snls_sn + ' zhel='+str(dic[snls_sn]['Z_HELIO']))
    plt.xlabel('Date')
    plt.ylabel('Flux')



class dico_multi_SN:

    def __init__(self):

        self.dic={}
        for snls_sn in listSN:
            self.dic[snls_sn]={}


    def addSNetoDic(self):
   
        for snls_sn in listSN:
            print snls_sn
            data_string=read_list(snls_sn, SkipRows=26, delimiteur='  ')
            self.dic[snls_sn]=create_dico_for_one_sn(data_string)
            ajouter_entete(self.dic[snls_sn], snls_sn)



if __name__=="__main__":
    print '---------'
 #   list_file='lc-05D3hh.list'#lc-SDSS15467.list'

 #   CL=read_list(list_file, SkipRows=26, delimiteur='  ') #trouver un moyen de trouver le nbre de lignes a sauter automatiquement
 #   dict_sn = create_dico_for_one_sn(CL)


   # plt.scatter(dict_sn['MEGACAMPSF::r']['Date'], dict_sn['MEGACAMPSF::r']['Flux'])
  

 #   plt.errorbar(dict_sn['MEGACAMPSF::g']['Date'], dict_sn['MEGACAMPSF::g']['Flux'], xerr=None, yerr=dict_sn['MEGACAMPSF::g']['Fluxerr'],linestyle='',alpha=0.75, marker='o', color='g', label='g')

 #   plt.errorbar(dict_sn['MEGACAMPSF::r']['Date'], dict_sn['MEGACAMPSF::r']['Flux'], xerr=None, yerr=dict_sn['MEGACAMPSF::r']['Fluxerr'],linestyle='',alpha=0.75, marker='o', color='r', label="r")

 #   plt.errorbar(dict_sn['MEGACAMPSF::i']['Date'], dict_sn['MEGACAMPSF::i']['Flux'], xerr=None, yerr=dict_sn['MEGACAMPSF::i']['Fluxerr'],linestyle='',alpha=0.75, marker='o', color='k', label='i')

 #   plt.errorbar(dict_sn['MEGACAMPSF::z']['Date'], dict_sn['MEGACAMPSF::z']['Flux'], xerr=None, yerr=dict_sn['MEGACAMPSF::z']['Fluxerr'],linestyle='',alpha=0.75, marker='o', color='b', label='z')
 #   plt.legend()
 #   plt.title('Courbe de lumiere lc-05D3hh')
 #   plt.xlabel('Date')
 #   plt.ylabel('Flux')


    AA=dico_multi_SN()
    AA.addSNetoDic()

    snls_sn='lc-05D3hh.list'
    print AA.dic[snls_sn].keys()
    plot_snls_light_curve(AA.dic, snls_sn, couleurs=['r','g','i'])
    plt.show()
