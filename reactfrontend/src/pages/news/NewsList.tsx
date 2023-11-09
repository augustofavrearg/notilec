import { IonButtons, IonContent, IonHeader, IonMenuButton, IonPage, IonTitle, IonToolbar, IonGrid, IonRow, IonCol, IonCard, IonItem, IonCardTitle, IonCardContent, IonLabel } from '@ionic/react';
import { useParams, useHistory } from 'react-router';
import ExploreContainer from '../../components/ExploreContainer';
import { IonButton } from '@ionic/react';
import { useEffect, useState } from 'react';
import { searchNews } from './NewsApi';
import News from './News';
import './NewsList.css'

const NewsList: React.FC = (props: any) => {

  const { name } = useParams<{ name: string; }>();

  const [newss, setNews] = useState<News[]>([]);

  const history = useHistory();

  useEffect(() => {
    search();
  }, [history.location.pathname]);

  const search = async () => {
    let resultado = await searchNews();
    setNews(resultado);
  }

  


  return (
    <IonPage>

      <IonHeader>
        <IonToolbar>
            <IonTitle className='titulo-noticias'>Noticias Argentina</IonTitle>
            <IonItem>
                <IonButton color="primary" size="default" fill="solid"  slot="end">Inicia Sesion</IonButton>
            </IonItem>
          <IonButtons slot="start">
            <IonMenuButton />
          </IonButtons>
          <IonTitle>{name}</IonTitle>
        </IonToolbar>
      </IonHeader>



      <IonContent fullscreen>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">{name}</IonTitle>
          </IonToolbar>
        </IonHeader>

        <IonCard>
            
            
            <IonGrid className="table">
                
            {newss.map((noticia: News) => 
                <IonRow>
                <IonCol>
                    <IonCardTitle>
                        <IonCardTitle>{noticia.titulo}</IonCardTitle>
                        <IonLabel>#{noticia.id}</IonLabel>
                    </IonCardTitle>
                    <IonCardContent>
                        {noticia.contenido}
                    </IonCardContent>
                    
                </IonCol>
                </IonRow>
              )}
                
                
                
            </IonGrid>
            
        </IonCard>

      </IonContent>

    </IonPage>
  );
};

export default NewsList;
