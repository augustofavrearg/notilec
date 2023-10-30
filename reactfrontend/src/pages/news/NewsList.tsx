import { IonButtons, IonContent, IonHeader, IonMenuButton, IonPage, IonTitle, IonToolbar, IonGrid, IonRow, IonCol, IonCard, IonItem, IonCardTitle, IonCardContent } from '@ionic/react';
import { useParams } from 'react-router';
import ExploreContainer from '../../components/ExploreContainer';
import { IonButton } from '@ionic/react';
import { useEffect, useState } from 'react';
import { saveNews, searchNews } from './NewsApi';

const NewsList: React.FC = () => {

  const { name } = useParams<{ name: string; }>();

  const [news, setNews] = useState<any>([]);

  useEffect(() => {
    search();
  }, []);

  const search = () =>{

    let resultado = searchNews();
    setNews(resultado);
  }

  const pruebaLocalStorage = () =>{
    const ejemplo = {
        dato:"dati",
        hora:"123"
    }
    saveNews(ejemplo);
  }

  return (
    <IonPage>

      <IonHeader>
        <IonToolbar>
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
            
            <IonTitle>Noticias Argentina</IonTitle>
            <IonItem>
                <IonButton color="primary" size="default" fill="solid"  slot="end">Inicia Sesion</IonButton>
            </IonItem>
            <IonGrid className="table">
                
            {news.map((item) => (
                <IonRow key={item.id}>
                <IonCol>
                    <IonCardTitle>
                        <IonCardTitle>{item.title}</IonCardTitle>
                    </IonCardTitle>
                    <IonCardContent>
                        {item.body}
                    </IonCardContent>
                    
                </IonCol>
                </IonRow>
            ))}
                
                
                
            </IonGrid>
            <IonItem>
                <IonButton onClick={pruebaLocalStorage} color="primary" size="default" fill="solid"  slot="end">genera Storage</IonButton>
            </IonItem>
        </IonCard>

      </IonContent>

    </IonPage>
  );
};

export default NewsList;
